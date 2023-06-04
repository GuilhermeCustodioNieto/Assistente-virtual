from audio_manager import *
import speech_recognition as sr
import sounddevice as sd
import wavio as wv
import pyttsx3
import commands
from audio_manager import *
import webbrowser


def gretting():
    iafala('Olá, como você vai? ')

def criador():
    iafala('Sou um assistente virtual criado por Guilherme Custodio Nieto')

def pesquisa(url):
    urlGoogle = f'https://www.google.com/search?g= {url}'
    webbrowser.open(urlGoogle, new=0, autoraise=True)

def exit():
    iafala('fechando o programa')



