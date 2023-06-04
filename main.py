import speech_recognition as sr
import sounddevice as sd
import wavio as wv
import pyttsx3
import commands
from audio_manager import *

MAX_TENTATIVAS = 1

while True:
    grava()
    r = sr.Recognizer()
    filename = 'voz.wav'
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        tentativa = 1
        text = retry_recognition(audio_data, r, MAX_TENTATIVAS)
        while text is None and tentativa < MAX_TENTATIVAS:
            iafala('Não entendi, fale novamente')
            grava()
            audio_data = r.record(source)
            text = retry_recognition(audio_data, r, MAX_TENTATIVAS)
            tentativa += 1

        if text is None:
            iafala('Não foi possível reconhecer o áudio, tente novamente')
            continue

        

        fala = text
        
        print(f'Você disse: {fala}')
        if fala == 'Olá':
            commands.gretting()

        elif 'bloco de notas' in fala:
            notas = fala.split('bloco de notas')

            with open('notas.txt', 'a+') as arquivo:
                arquivo.write(f'{notas}\n')


        elif fala == 'quem é seu Criador':
            commands.criador()
        elif fala == 'sair':
            commands.exit()
            break

print('Fim do programa')
