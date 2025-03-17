#Crie um progama que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# num = int(input('Digite um número :'))
# if num % 2  :
#     print('O número digitado é Ímpar!')
# else :
#     print('O número digitado é Par!')
#############################################
numero = int(input('Digite um número :'))
resultado = numero % 2
if resultado == 0:
    print('O número digitado é PAR!')
else:
    print('O número digitado é IMPAR!')