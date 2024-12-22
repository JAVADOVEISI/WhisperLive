from whisper_live.client import TranscriptionClient

client = TranscriptionClient(
    host="localhost",               # Server host
    port=9090,                      # Server port
    lang="en",                      # Language of the input audio
    translate=False,                # Set to True to translate to English
    model="small",                  # Whisper model size
    use_vad=False,                  # Use Voice Activity Detection
    save_output_recording=True,     # Save microphone input as a .wav file
    output_recording_filename="./output_recording.wav",  # Filename for saved recording
    max_clients=4,                  # Maximum number of clients
    max_connection_time=600         # Maximum connection time in seconds
)

# Transcribe an audio file
client("tests/jfk.wav")

# Transcribe from the microphone
client()