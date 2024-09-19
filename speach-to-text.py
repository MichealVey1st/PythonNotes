import pyaudio
import wave
import threading
import keyboard  
import whisper

# Function to handle recording
import pyaudio
import wave

def record_audio(filename):
    # Set up audio parameters
    chunk = 1024  # Record in chunks of 1024 samples
    format = pyaudio.paInt16  # 16-bit resolution
    channels = 1  # Mono audio
    rate = 44100  # 44.1 kHz sampling rate
    p = pyaudio.PyAudio()
    
    # Open the stream
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)
    
    print("Recording... Press ESC again to stop.")
    frames = []

    try:
        while not stop_recording:
            data = stream.read(chunk)
            frames.append(data)
    except KeyboardInterrupt:
        print("Recording interrupted.")
    
    # Stop recording
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the audio to a file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
    
    print(f"Audio saved to {filename}")

    transcribe_audio(filename)



def transcribe_audio(filename):
    print("Transcribing...")
    # Load the model
    model = whisper.load_model("base")

    # Transcribe the audio file
    result = model.transcribe(filename)
    
    # Ensure the result is a dictionary and extract the transcription text
    if isinstance(result, dict) and 'text' in result:
        transcription_text = result['text']
    else:
        raise ValueError("Unexpected result format from transcription")

    # Ensure transcription_text is a string
    if isinstance(transcription_text, list):
        transcription_text = " ".join(transcription_text)
    elif not isinstance(transcription_text, str):
        raise ValueError("Transcription text is not a string")

    # Save transcription to a file
    transcript_filename = filename.replace(".wav", "_transcript.txt")
    with open(transcript_filename, 'w') as f:
        f.write(transcription_text)
    
    print(f"Transcription saved to {transcript_filename}")

# Start and stop recording on key press
def start_stop_recording():
    global stop_recording
    audio_filename = "continuous_recording.wav"
    print("ready to record....")
    
    while True:
        # Wait for ESC to start recording
        keyboard.wait('esc')
        stop_recording = False
        print("Starting recording...")
        
        # Start recording in a thread
        record_thread = threading.Thread(target=record_audio, args=(audio_filename,))
        record_thread.start()
        
        # Wait for ESC to stop recording
        keyboard.wait('esc')
        stop_recording = True
        record_thread.join()  # Wait for the recording to finish

# Global flag to control recording
stop_recording = True

# Start the process
#start_stop_recording()
transcribe_audio('continuous_recording.wav')