#Façaum progama que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.o progama deverá escrever o nome na tela se o usuário venceu ou perdeu.

import math

import random


print('Jogo de Adivinhação :')
print('o computador esta pensando em um número...')
import time

def contador(segundos):
    for i in range(segundos):
        min,seg = divmod(segundos-i, 60)
        texto = f'{min:02d}:{seg:02d}'
        print(texto,end='\r')
        time.sleep(1)
contador(5)


usuario = int(input('De 0 a 5 qual, número voce acha que o computador pensou, Digite : '))

num = random.randint(0, 5)
print(f'Computador pensou no número:{num}')
if num == usuario :
    print('PARABENS VOCÊ ACERTOUUU!!!')
else :
    print('NÃO FOI DESSA VEZ!')