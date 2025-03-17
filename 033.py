#Faça um  progama que leia três números e mostre qual é o MAIOR e qual é o MENOR.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
#verificando qual é o maior:
maior = a
if b > a and c:
   maior = b
if c > b and a:
   maior = c
print(f'O maior número digitado foi: {maior}')
#Verificando qual é o menor:
menor = a
if b < a and c:
    menor = b
if c < b and a:
    menor = c
print(f'O menor número digitado foi: {menor}')
    
