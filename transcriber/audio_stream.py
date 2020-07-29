import pyaudio

CHUNK_SIZE = 4096
RATE = 44100
DEVICE_NAME_CONTAINS = 'Realtek'
INPUT_INDEX = 0


def open_audio_stream():
    global INPUT_INDEX
    
    p = pyaudio.PyAudio()

    # Find audio input device
    info = p.get_host_api_info_by_index(0)
    num_devices = info.get('deviceCount')

    for i in range(num_devices):
        device_name = p.get_device_info_by_host_api_device_index(0, i).get('name')

        if 'Microphone' in device_name and DEVICE_NAME_CONTAINS in device_name:
            INPUT_INDEX = i

    # Create stream
    return p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK_SIZE,
        input_device_index=INPUT_INDEX
    )