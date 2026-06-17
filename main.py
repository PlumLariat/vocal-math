import sounddevice as sd
import soundfile as sf
from queue import Queue
from vosk import Model, KaldiRecognizer
import wave
from word2number import w2n
import json

# configuration
fs = 44100
filename = "sound_data.wav"
audio_queue = Queue()

def callback(indata, frames, time, status):
    """Callback function to push audio chunks into queue."""
    if status:
        print(status)
    audio_queue.put(indata.copy())


def main():
    try:
        # Open a file for writing
        with sf.SoundFile(filename, mode='w', samplerate=fs, channels=1) as file:
            # start the microphone stream
            with sd.InputStream(samplerate=fs, channels=1, callback=callback):
                print(f"Recording to: {filename}\nPress Ctrl+C to stop.")
                while True:
                    # Pull chunks from queue and write directly to disk
                    file.write(audio_queue.get())
                    
    except KeyboardInterrupt:
        print(f"\nRecording Stopped. File saved as: {filename}")
        # load model from local directory
        model = Model("vosk-model-small-en-us-0.15")

        # Open the audio file
        wf = wave.open(filename, "rb")

        # Initialize the recognizer with the model and audio sample rate
        rec = KaldiRecognizer(model, wf.getframerate())

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                print(rec.Reset())
            else:
                print(rec.PartialResult())

        # print results
        print("Final Result")
        data = json.loads(rec.FinalResult())
        print(data["text"])
        print(w2n.word_to_num(data['text']))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
