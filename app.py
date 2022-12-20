import os
import argparse

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton


data_X = -1
data_Y = -1
mel_spec = None
fig = None
axes = None
min = None


def plot_mel(data, titles):
    fig, axes = plt.subplots(len(data), 1, squeeze=False)
    if titles is None:
        titles = [None for i in range(len(data))]

    for i in range(len(data)):
        mel = data[i]
        axes[i][0].imshow(mel, origin="lower")
        axes[i][0].set_aspect(2.5, adjustable="box")
        axes[i][0].set_ylim(0, mel.shape[0])
        axes[i][0].set_title(titles[i], fontsize="medium")
        axes[i][0].tick_params(labelsize="x-small", left=False, labelleft=False)
        axes[i][0].set_anchor("W")

    return fig, axes


def on_move(event):
    global data_X, data_Y
    if event.inaxes:
        data_X = event.xdata
        data_Y = event.ydata


def on_click(event):
    global plt, axes, mel_spec, min
    if event.button is MouseButton.LEFT:
        mel_spec[int(data_Y)][int(data_X)] = min
        axes[0][0].imshow(mel_spec, origin="lower")
        fig.canvas.draw()
        fig.canvas.flush_events()


def main(filepath):
    global mel_spec, fig, axes, min

    mel_spec = np.load(filepath).T
    min = np.min(mel_spec.flatten())

    fig, axes = plot_mel([mel_spec], None)

    plt.connect('motion_notify_event', on_move)
    plt.connect('button_press_event', on_click)

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--orig_npy_filepath", type=str, required=True, default=None, help="path to original file")
    # parser.add_argument("--output_npy_filepath", type=str, required=True, default=None, help="path to edited npy file")
    args = parser.parse_args()
    main(args.orig_npy_filepath)