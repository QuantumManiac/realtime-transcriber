import numpy as np
from transcriber.settings import CHUNK_SIZE, RATE
from scipy.fftpack import fft, fftfreq


def process_stream(stream):
    read_data = stream.read(CHUNK_SIZE)
    data = np.frombuffer(read_data, dtype=np.int16)

    # Compute fft and retrieve its frequencies
    fourier = fft(data)
    fourier_freq = fftfreq(CHUNK_SIZE) * RATE

    # Halve list to get rid of negative frequencies
    fourier = fourier[:len(data) // 2]
    fourier_freq = fourier_freq[:len(data) // 2]

    # Remove first item to get rid of 0 Hz values
    fourier = fourier[1:]
    fourier_freq = fourier_freq[1:]

    # Get rid of complex values
    fourier = [abs(i) for i in fourier]

    # Halve all frequency values (No idea why it's double in the first place)
    fourier_freq = [i / 2 for i in fourier_freq]

    return data, fourier, fourier_freq
