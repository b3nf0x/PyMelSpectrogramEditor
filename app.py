import os
import argparse

import numpy as np


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--orig_npy_filepath", type=str, required=True, default=None, help="path to original file")
    parser.add_argument("--output_npy_filepath", type=str, required=True, default=None, help="path to edited npy file")
    args = parser.parse_args()

    mel_spec = np.load(args.orig_npy_filepath)
    if not mel_spec:
        print("npy file loading failed")
        os.exit(1)

    