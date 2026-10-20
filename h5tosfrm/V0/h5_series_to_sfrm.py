#!/usr/bin/env python3
"""
Convert  <prefix>_<filenumber>.h5  ->  <prefix>_<NN>_<IIII>.sfrm  (Bruker FORMAT 100).

  * NN   = file number, zero-padded to 2 digits
  * IIII = image number (1-based), zero-padded to 4 digits

Header handling
  1. The full header is copied from calibration.sfrm into every output frame.
  2. RANGE, START, INCREME, ANGLES, ENDING are entered by you for frame #1:
         --range --start --increme --angles A1 A2 A3 A4 --ending E1 E2 E3 E4
     (anything you leave out is asked for interactively).
  3. For frame #N (N >= 2):
         RANGE    = RANGE of #1                 (unchanged)
         INCREME  = INCREME of #1               (unchanged)
         ANGLES   = ENDING of frame #N-1
         START    = START of frame #N-1 + INCREME
         ENDING   = ENDING of frame #N-1 + INCREME on the scan axis
                    (other angles keep their ENDING value from #1)
     The scan axis is the angle that differs between your ANGLES and ENDING for
     frame #1; if none differ, it is taken from the AXIS key of calibration.sfrm
     (1=2theta, 2=omega, 3=phi, 4=chi). Override with --axis.

ANGLES / ENDING order: 2theta omega phi chi.

Because the pixel data change per frame, these keys are also refreshed so the
file stays valid: NOVERFL, NCOUNTS, MINIMUM, MAXIMUM, NUMBER, NFRAMES, FILENAM.

Example
  python h5_series_to_sfrm.py sample_03.h5 -c calibration.sfrm \\
      --range 0.5 --start 35 --increme 0.5 \\
      --angles 0 0 35 0 --ending 0 0 35.5 0
"""
import argparse
import os
import re
import sys

import h5py
import numpy as np

try:  # registers compression filters (bitshuffle/LZ4, Blosc, ...) used by Dectris/Eiger files
    import hdf5plugin  # noqa: F401
except ImportError:
    hdf5plugin = None

try:  # fabio (pip install fabio) also pulls in hdf5plugin
    import fabio
except ImportError:
    fabio = None

CARD = 80
BLOCK = 512
AXIS_NAMES = {"2theta": 0, "omega": 1, "phi": 2, "chi": 3}
GAP_VALUE = 0xFFFFFFFF   # gap pixels (as in APEX-written Pilatus frames)
HOT_VALUE = 0xFFFFFFFE   # hot pixels


# ------------------------------------------------------------------ header
def read_header_cards(path):
    raw = open(path, "rb").read()
    hdrblks = None
    for i in range(0, 20 * CARD, CARD):
        c = raw[i:i + CARD].decode("latin-1")
        if c.startswith("HDRBLKS"):
            hdrblks = int(c[8:].split()[0])
            break
    if hdrblks is None:
        sys.exit("HDRBLKS not found in %s; is it a Bruker sfrm file?" % path)
    hdr = raw[:hdrblks * BLOCK]
    return [hdr[i:i + CARD].decode("latin-1") for i in range(0, len(hdr), CARD)]


def get(cards, key):
    for c in cards:
        if c[:7].strip() == key and c[7:8] == ":":
            return c[8:].strip()
    return None


def set_card(cards, key, value):
    for i, c in enumerate(cards):
        if c[:7].strip() == key and c[7:8] == ":":
            cards[i] = (key.ljust(7) + ":" + value).ljust(CARD)[:CARD]
            return
    sys.exit("Key %s not found in calibration header" % key)


def fmt_angles(a):
    return "".join("%-18.6f" % (0.0 if abs(v) < 5e-7 else v) for v in a).rstrip()


def fmt_num(v):
    return "%.6f" % (0.0 if abs(v) < 5e-7 else v)


# ------------------------------------------------------------ pixel coding
def _pad16(b):
    return b + b"\0" * ((-len(b)) % 16)


def encode_pixels(img):
    flat = img.ravel()
    d8 = np.minimum(flat, 255).astype(np.uint8)
    big = flat[flat >= 255]
    t16 = np.where(big >= 65535, 65535, big).astype("<u2")
    t32 = big[big >= 65535].astype("<u4")
    blob = d8.tobytes() + _pad16(t16.tobytes()) + _pad16(t32.tobytes())
    return blob, len(t16), len(t32)


def frame_stats(img):
    good = img < HOT_VALUE
    if not good.any():
        return 0, 0, 0
    g = img[good]
    return int(g.sum(dtype=np.uint64)), int(g.min()), int(g.max())


def to_uint32(frame):
    if frame.dtype.kind == "i":      # -1 = gap, -2 = hot pixel
        v = frame.astype(np.int64)
        v = np.where(v < 0, np.where(v == -2, HOT_VALUE, GAP_VALUE), v)
        return v.astype(np.uint32)
    if frame.dtype.kind == "u":      # max value of the dtype = gap
        v = frame.astype(np.uint64)
        v = np.where(v >= np.iinfo(frame.dtype).max, GAP_VALUE, v)
        return v.astype(np.uint32)
    return np.clip(np.rint(frame), 0, HOT_VALUE - 1).astype(np.uint32)


# -------------------------------------------------------------------- HDF5
def find_frame_datasets(h5, nrows, ncols):
    hits = []

    def visit(name, obj):
        if isinstance(obj, h5py.Dataset) and obj.ndim == 3 \
                and tuple(obj.shape[1:]) in ((nrows, ncols), (ncols, nrows)):
            hits.append(name)

    h5.visititems(visit)
    return sorted(hits)


# ------------------------------------------------------------ frame readers
def _read_error(e):
    sys.exit("Cannot read image data (%s).\n"
             "The data are probably compressed with a filter h5py does not include "
             "(e.g. bitshuffle+LZ4).\nFix:  pip install fabio   (it installs hdf5plugin)\n"
             "or:   pip install hdf5plugin" % e)


def open_source(args, nrows, ncols):
    """Return (nframes, iterator_of_2D_arrays, close_function)."""
    use_fabio = (args.reader == "fabio") or (args.reader == "auto" and fabio is not None
                                             and not args.dataset)
    if args.reader == "fabio" and fabio is None:
        sys.exit("fabio is not installed:  pip install fabio")

    if use_fabio:
        im = fabio.open(args.h5file)
        n = im.nframes
        print("Found %d images (read with fabio, %s)" % (n, type(im).__name__))

        def gen():
            for k in range(n):
                try:
                    yield im.getframe(k).data
                except OSError as e:
                    _read_error(e)
        return n, gen(), im.close

    f = h5py.File(args.h5file, "r")
    names = args.dataset or find_frame_datasets(f, nrows, ncols)
    if not names:
        sys.exit("No 3D dataset of shape (N,%d,%d) found; use --dataset" % (nrows, ncols))
    dsets = [f[n] for n in names]
    n = sum(d.shape[0] for d in dsets)
    print("Found %d images in %s (read with h5py)" % (n, ", ".join(names)))

    def gen():
        for d in dsets:
            for k in range(d.shape[0]):
                try:
                    yield d[k]
                except OSError as e:
                    _read_error(e)
    return n, gen(), f.close


# ------------------------------------------------------------------- input
def ask_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("  please enter a number")


def ask_four(prompt):
    while True:
        try:
            v = [float(x) for x in input(prompt).replace(",", " ").split()]
            if len(v) == 4:
                return v
        except ValueError:
            pass
        print("  please enter four numbers: 2theta omega phi chi")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("h5file", help="<prefix>_<filenumber>.h5")
    ap.add_argument("-c", "--calibration", default="calibration.sfrm")
    ap.add_argument("-o", "--outdir", help="output folder (default: folder of the h5 file)")
    ap.add_argument("--range", type=float, dest="range_")
    ap.add_argument("--start", type=float)
    ap.add_argument("--increme", type=float)
    ap.add_argument("--angles", type=float, nargs=4, metavar=("TTH", "OMG", "PHI", "CHI"))
    ap.add_argument("--ending", type=float, nargs=4, metavar=("TTH", "OMG", "PHI", "CHI"))
    ap.add_argument("--axis", choices=list(AXIS_NAMES), help="scan axis (default: auto)")
    ap.add_argument("--reader", choices=["auto", "fabio", "h5py"], default="auto",
                    help="how to read the HDF5 images (auto: fabio if installed, else h5py; "
                         "--dataset forces h5py)")
    ap.add_argument("--dataset", action="append",
                    help="HDF5 dataset path (repeatable); default: auto-detect")
    ap.add_argument("--transpose", action="store_true")
    ap.add_argument("--flipud", action="store_true")
    ap.add_argument("--fliplr", action="store_true")
    args = ap.parse_args()

    # ---- file name -> prefix, 2-digit file number
    base = os.path.basename(args.h5file)
    m = re.match(r"^(.*)_(\d+)\.h5$", base, re.IGNORECASE)
    if not m:
        sys.exit("Input name must look like <prefix>_<number>.h5, got %s" % base)
    prefix, filenum = m.group(1), int(m.group(2))
    outdir = args.outdir or (os.path.dirname(os.path.abspath(args.h5file)))
    os.makedirs(outdir, exist_ok=True)

    # ---- manual values for frame #1
    range_ = args.range_ if args.range_ is not None else ask_float("RANGE   : ")
    start = args.start if args.start is not None else ask_float("START   : ")
    increme = args.increme if args.increme is not None else ask_float("INCREME : ")
    angles1 = args.angles or ask_four("ANGLES (2theta omega phi chi): ")
    ending1 = args.ending or ask_four("ENDING (2theta omega phi chi): ")

    # ---- calibration header
    cal = read_header_cards(args.calibration)
    nrows = int(get(cal, "NROWS").split()[0])
    ncols = int(get(cal, "NCOLS").split()[0])

    # ---- scan axis
    if args.axis:
        axis = AXIS_NAMES[args.axis]
    else:
        diff = [i for i in range(4) if abs(ending1[i] - angles1[i]) > 1e-9]
        if len(diff) == 1:
            axis = diff[0]
        else:
            axis = int(get(cal, "AXIS").split()[0]) - 1
    axis_name = [k for k, v in AXIS_NAMES.items() if v == axis][0]
    print("Scan axis used for ENDING progression: %s" % axis_name)
    if abs((ending1[axis] - angles1[axis]) - increme) > 1e-9:
        print("WARNING: ENDING-ANGLES on the scan axis (%.6f) differs from INCREME (%.6f)"
              % (ending1[axis] - angles1[axis], increme))

    nframes, frames, closer = open_source(args, nrows, ncols)
    try:
        # ---- per-frame header values
        starts, angles, endings = [], [], []
        for i in range(nframes):
            starts.append(start + i * increme)
            e = list(ending1)
            e[axis] = ending1[axis] + i * increme
            endings.append(e)
            angles.append(list(angles1) if i == 0 else list(endings[i - 1]))

        i = 0
        for img in frames:
            img = np.asarray(img)
            if img.shape == (ncols, nrows) and nrows != ncols:
                img = img.T
            if args.transpose:
                img = img.T
            if args.flipud:
                img = img[::-1]
            if args.fliplr:
                img = img[:, ::-1]
            if img.shape != (nrows, ncols):
                sys.exit("frame shape %s != calibration (%d,%d); try --transpose"
                         % (img.shape, nrows, ncols))
            img = to_uint32(img)

            name = "%s_%02d_%04d.sfrm" % (prefix, filenum, i + 1)
            c = list(cal)
            set_card(c, "RANGE", fmt_num(range_))
            set_card(c, "START", fmt_num(starts[i]))
            set_card(c, "INCREME", fmt_num(increme))
            set_card(c, "ANGLES", fmt_angles(angles[i]))
            set_card(c, "ENDING", fmt_angles(endings[i]))

            blob, n16, n32 = encode_pixels(img)
            total, mn, mx = frame_stats(img)
            set_card(c, "NOVERFL", "%-24d%-24d%d" % (-1, n16, n32))
            set_card(c, "NCOUNTS", "%-44d%d" % (total, 0))
            set_card(c, "MINIMUM", str(mn))
            set_card(c, "MAXIMUM", str(mx))
            set_card(c, "NUMBER", str(i + 1))
            set_card(c, "NFRAMES", str(nframes))
            set_card(c, "FILENAM", name)

            with open(os.path.join(outdir, name), "wb") as out:
                out.write("".join(c).encode("latin-1"))
                out.write(blob)
            i += 1
            if i % 50 == 0 or i == nframes:
                print("wrote %d/%d  %s" % (i, nframes, name))
    finally:
        closer()


if __name__ == "__main__":
    main()
