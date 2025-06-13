import os
import wave 
import json
from vosk import Model, KaldiRecognizer
import pyaudio



# Initializing Vosk Model
model = Model("models/vosk-model-small-en-in-0.4/")
recognizer = KaldiRecognizer(model, 16000)

# Recording audio from the mic
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)

print("Listening...")

while True:
    data = stream.read(4000)
    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        text = json.loads(result)['text']
        print(f"Recognized text : {text}")
