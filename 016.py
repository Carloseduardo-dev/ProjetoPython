#Crie um progama que leia um número real qualquer epelo teclado e mostre na tela a sua porção inteira.

import math
num = float(input('Digite um número :'))
truncado = math.trunc(num)
print(truncado)