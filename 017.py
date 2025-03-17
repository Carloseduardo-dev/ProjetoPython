#Faça um progama que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo , calcule e mostre o comprimento da hipotenusa.
co = float(input('quanto mede o cateto oposto ? '))
ca = float(input('quanto mede o cateto adjacente ? '))
ipo = (co**2 + ca**2) ** 1/5
print(ipo)
print('='*30)
import math
co = float(input('Quanto mede o cateto oposto :'))
ca = float(input('Quanto mede o cateto adjacente :'))
ipo = math.hypot(ipo)
print(ipo)