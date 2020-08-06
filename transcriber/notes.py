NOTES = {16.35: "C-0", 18.35: "D-0", 20.6: "E-0", 21.83: "F-0", 24.5: "G-0", 27.5: "A-0", 30.87: "B-0", 32.7: "C-1",
         36.71: "D-1", 41.2: "E-1", 43.65: "F-1", 49: "G-1", 55: "A-1", 61.74: "B-1", 65.41: "C-2", 73.42: "D-2",
         82.41: "E-2", 87.31: "F-2", 98: "G-2", 110: "A-2", 123.47: "B-2", 130.81: "C-3", 146.83: "D-3", 164.81: "E-3",
         174.61: "F-3", 196: "G-3", 220: "A-3", 246.94: "B-3", 261.63: "C-4", 293.66: "D-4", 329.63: "E-4",
         349.23: "F-4", 392: "G-4", 440: "A-4", 493.88: "B-4", 523.25: "C-5", 587.33: "D-5", 659.25: "E-5",
         698.46: "F-5", 783.99: "G-5", 880: "A-5", 987.77: "B-5", 1046.5: "C-6", 1174.66: "D-6", 1318.51: "E-6",
         1396.91: "F-6", 1567.98: "G-6", 1760: "A-6", 1975.53: "B-6", 2093: "C-7", 2349.32: "D-7", 2637.02: "E-7",
         2793.83: "F-7", 3135.96: "G-7", 3520: "A-7", 3951.07: "B-7", 4186.01: "C-8", 4698.63: "D-8", 5274.04: "E-8",
         5587.65: "F-8", 6271.93: "G-8", 7040: "A-8", 7902.13: "B-8"}

'''
SHARPS_AND_FLATS = {17.32: "C#-0/Db-0", 19.45: "D#-0/Eb-0", 23.12: "F#-0/Gb-0", 25.96: "G#-0/Ab-0", 29.14: "A#-0/Bb-0",
                    34.65: "C#-1/Db-1", 38.89: "D#-1/Eb-1", 46.25: "F#-1/Gb-1", 51.91: "G#-1/Ab-1", 58.27: "A#-1/Bb-1",
                    69.3: "C#-2/Db-2", 77.78: "D#-2/Eb-2", 92.5: "F#-2/Gb-2", 103.83: "G#-2/Ab-2", 116.54: "A#-2/Bb-2",
                    138.59: "C#-3/Db-3", 155.56: "D#-3/Eb-3", 185: "F#-3/Gb-3", 207.65: "G#-3/Ab-3", 
                    233.08: "A#-3/Bb-3", 277.18: "C#-4/Db-4", 311.13: "D#-4/Eb-4", 369.99: "F#-4/Gb-4", 
                    415.3: "G#-4/Ab-4", 466.16: "A#-4/Bb-4", 554.37: "C#-5/Db-5", 622.25: "D#-5/Eb-5", 
                    739.99: "F#-5/Gb-5", 830.61: "G#-5/Ab-5", 932.33: "A#-5/Bb-5", 1244.51: "D#-6/Eb-6",
                    1479.98: "F#-6/Gb-6", 1661.22: "G#-6/Ab-6", 1864.66: "A#-6/Bb-6", 2489.02: "D#-7/Eb-7", 
                    2959.96: "F#-7/Gb-7", 3322.44: "G#-7/Ab-7", 3729.31: "A#-7/Bb-7", 4434.92: "C#-8/Db-8", 
                    4978.03: "D#-8/Eb-8", 6644.88: "G#-8/Ab-8", 7458.62: "A#-8/Bb-8"}
'''

combo = 0
prev_note = None
notes_dict = NOTES


# if USE_SHARPS_AND_FLATS:
#     notes_dict.update(SHARPS_AND_FLATS)


def identify_note(fourier, freqs):
    global combo
    global prev_note

    max_fft_val = max(fourier)
    largest_freq = freqs[fourier.index(max_fft_val)]

    most_likely_note_freq = min(notes_dict.keys(), key=lambda n: abs(largest_freq - n))

    print(most_likely_note_freq, prev_note, combo)

    # Restricting accepted range to 25 < f < 4500 to get rid of anything above C8 and below A0
    if most_likely_note_freq == prev_note and 25 < most_likely_note_freq < 4500:
        combo += 1
    else:
        combo = 0

    prev_note = most_likely_note_freq

    return most_likely_note_freq, largest_freq, combo


def get_loudness(data):
    return max(data)
