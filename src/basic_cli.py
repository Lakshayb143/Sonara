import json
import os
from datetime import datetime

import pyaudio
import spacy
from TTS.api import TTS
from vosk import KaldiRecognizer, Model

# Initialize components
model = Model("../models/vosk-model-small-en-in-0.4/")  # Path to Vosk model
recognizer = KaldiRecognizer(model, 16000)
nlp = spacy.load("en_core_web_sm")
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", gpu=False)

# Function to record speech and recognize text
def listen():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)

    print("Listening...")

    while True:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result)["text"]
            print(f"Recognized: {text}")
            return text

# Process the recognized command using NLP
def process_command(command):
    doc = nlp(command)
    if "time" in command:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
    elif "joke" in command:
        return "Why don’t skeletons fight each other? They don’t have the guts!"
    return "This is Lakshay's Personal assistant"

# Convert text to speech and respond
def speak(text):
    # tts.tts_to_file(text, "response.wav",speaker="some_speaker")
    tts.tts_to_file(text=text, file_path="response.wav")
    os.system("aplay response.wav")

if __name__ == "__main__":
    while True:
        command = listen()
        response = process_command(command)
        speak(response)
