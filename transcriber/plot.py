import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import mingus.extra.lilypond as LilyPond
import numpy as np
from mingus.containers import Bar, Track

from transcriber.notes import notes_dict
from transcriber.settings import CHUNK_SIZE, LOUDNESS_THRESHOLD, MINIMUM_FREQUENCY

prev_loudness = 0

fig = None
ax1 = None
ax2 = None
ax3 = None
line1 = None
line2 = None
sheet = None
t = Track()


def setup_plotting():
    global fig
    global ax1
    global ax2
    global ax3
    global line1
    global line2
    global sheet

    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(2, 2, 1)  # Volume
    ax2 = fig.add_subplot(2, 2, 2)  # Fourier
    ax3 = fig.add_subplot(2, 1, 2)  # Notes
    ax3.set_axis_off()

    line1, = ax1.plot(np.random.randn(CHUNK_SIZE))
    line2, = ax2.plot(np.random.randn(CHUNK_SIZE))

    b = Bar()
    bar = LilyPond.from_Bar(b)
    LilyPond.to_png(bar, "track")
    img = mpimg.imread("track.png")
    cropped_image = img[0:300, :, :]
    sheet = ax3.imshow(cropped_image, cmap='gray', interpolation='antialiased')


def update_plot(data, fourier, freqs):
    global ax1
    global ax2
    global line1
    global line2

    line1.set_ydata(data)
    line2.set_xdata(freqs)
    line2.set_ydata(fourier)

    ax1.set_xlim(0, CHUNK_SIZE)
    ax1.set_ylim(-255, 255)
    ax2.set_xlim(0, CHUNK_SIZE)
    ax2.set_ylim(0, 10000)

    plt.pause(0.001)


def update_plot_with_note(largest_freq, note_freq):
    if largest_freq > MINIMUM_FREQUENCY:
        ax2.set_title(
            f"The largest frequency is {(largest_freq):.2f} Hz. Most likely note is {notes_dict[note_freq]} ({note_freq})")


def update_plot_with_loudness(loudness):
    ax1.set_title(f"Loudness: {loudness}. Threshold reached: {loudness >= LOUDNESS_THRESHOLD}")


def update_sheet_music(note):
    dict_note = notes_dict[note]
    t.add_notes(dict_note)
    track = LilyPond.from_Track(t)
    LilyPond.to_png(track, "track")
    img = mpimg.imread("track.png")
    cropped_image = img[0:300, :, :]
    sheet.set_data(cropped_image)
