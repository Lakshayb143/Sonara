
from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", gpu=False)

def speak(text):
    tts.tts_to_file(text=text, file_path="response.wav")
    os.system("aplay response.wav")
