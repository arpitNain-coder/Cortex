import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen():
    fs = 44100
    duration = 8  # seconds

    print("Listening...")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype='int16'
    )

    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp:
        write(temp.name, fs, recording)

        recognizer = sr.Recognizer()

        with sr.AudioFile(temp.name) as source:
            audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError as e:
        print("Error:", e)
        return ""
