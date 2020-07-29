from transcriber.settings import *
from transcriber.audio_stream import open_audio_stream
from transcriber.process_stream import process_stream
from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

stream = open_audio_stream()

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 2)
ax2 = fig.add_subplot(2, 1, 1)
line1, = ax1.plot(np.random.randn(CHUNK_SIZE))
line2, = ax2.plot(np.random.randn(CHUNK_SIZE))


while True:
    data, fourier, fourier_freq = process_stream(stream)
    line1.set_ydata(data)
    line2.set_xdata(fourier_freq)
    line2.set_ydata(fourier)
    ax1.set_xlim(0, CHUNK_SIZE)
    ax1.set_ylim(-255, 255)
    ax2.set_xlim(0, CHUNK_SIZE)
    ax2.set_ylim(0, 10000)
    plt.pause(0.001)







