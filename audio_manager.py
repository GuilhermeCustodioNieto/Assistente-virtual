import speech_recognition as sr
import sounddevice as sd
import wavio as wv
import pyttsx3

def iafala(fala):
    engine = pyttsx3.init()
    engine.say(fala)
    engine.runAndWait()

def grava():
    freq = 48000
    duration = 5
    gravacao = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    print('fale agora')
    sd.wait()
    wv.write('voz.wav', gravacao, freq, sampwidth=2)
    print('processando')


def recognize_speech(audio_data, recognizer):
    try:
        text = recognizer.recognize_google(audio_data, language='pt-br')
        return text
    except sr.UnknownValueError:
        return None

def retry_recognition(audio_data, recognizer, max_tentativas):
    text = None
    text = recognize_speech(audio_data, recognizer)
    tentativas = 1
    while text is None and tentativas < max_tentativas:
        iafala('não entendi, fale novamente')
        text = recognize_speech(audio_data, recognizer)
        print(text)
        tentativas +=1
    return text