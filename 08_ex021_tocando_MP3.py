"""08_ex021_tocando_MP3.py em 2018-12-11. Projeto Curso em Video.

Tocando um MP3

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

"""
import pygame
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Tocando um MP3')

    print('''\timport pygame
    
    pygame.init()
    pygame.mixer.music.load('08_ex021.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    ''')
    pygame.init()
    pygame.mixer.music.load('08_ex021.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
