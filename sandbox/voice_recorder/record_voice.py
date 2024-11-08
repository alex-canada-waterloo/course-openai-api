import sounddevice as sd
from scipy.io.wavfile import write

import sounddevice as sd

# List all available audio input devices
print(sd.query_devices())


# Define recording parameters
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
filename = "recording.wav"  # Output file name

# Function to record audio
def record_audio():
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save the recording
    write(filename, sample_rate, audio_data)
    print(f"Recording saved as {filename}")

# Run the function
record_audio()