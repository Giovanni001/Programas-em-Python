'''
Exercício Python 021: Faça um programa em Python que abra e
reproduza o áudio de um arquivo MP3.
'''

from pygame import mixer
mixer.init()
mixer.music.load('Kalimba.mp3')
mixer.music.play()

input('Agora você escuta?')

print('Programa encerrado !')
