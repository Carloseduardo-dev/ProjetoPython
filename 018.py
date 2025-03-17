#Faça um progama que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse ângulo:
    
import math

angulo = float(input('Digite um ângulo qualquer e veja seu seno,cosseno e tangente :°'))
sen = math.sin(angulo)
co = math.cos(angulo)
tan = math.cos(angulo)
print(f'O seno desse ângulo mede {sen}\nseu cosseno mede {co} e sua tangente é de {tan} !')
