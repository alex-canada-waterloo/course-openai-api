import sounddevice as sd
from scipy.io.wavfile import read

# Define the filename
filename = "recording.wav"

# Load the audio file
sample_rate, audio_data = read(filename)

# Play the audio file
print("Playing audio...")
sd.play(audio_data, sample_rate)
sd.wait()  # Wait until playback is finished
print("Playback finished.")