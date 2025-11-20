#Façaum progama que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.o progama deverá escrever o nome na tela se o usuário venceu ou perdeu.

import math
import time
import random


print('Jogo de Adivinhação :')
print('o computador esta pensando em um número...')
import time

usuario = int(input('De 0 a 5 qual, número voce acha que o computador pensou, Digite : '))

for i in range(0, 10, -1):
    print(i)
    time.sleep(1)
num = random.randint(0, 5)
print(f'Computador pensou no número:{num}')
if num == usuario :
    print('PARABENS VOCÊ ACERTOUUU!!!')
else :
    print('NÃO FOI DESSA VEZ!')
