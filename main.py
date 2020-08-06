from transcriber.audio_stream import open_audio_stream
from transcriber.notes import identify_note, get_loudness
from transcriber.plot import *
from transcriber.process_stream import process_stream

prev_loudness = 0

stream = open_audio_stream()
setup_plotting()

while True:
    data, fourier, fourier_freq = process_stream(stream)

    note_freq, largest_freq, combo = identify_note(fourier, fourier_freq)

    update_plot_with_note(largest_freq, note_freq)

    loudness = get_loudness(data)
    update_plot_with_loudness(loudness)

    update_plot(data, fourier, fourier_freq)
    if combo == 3:
        update_sheet_music(note_freq)

    prev_loudness = loudness
