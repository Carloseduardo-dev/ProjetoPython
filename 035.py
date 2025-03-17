#Desenvolva um progama que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Digite o tamanho do 1° segmento de reta:'))
b = float(input('Digite o tamanho do 2° segmento de reta:'))
c = float(input('Digite o tamanho do 3° segmento de reta:'))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos PODEM FORMA triângulo!')
else:
    print('Os segmentos NÃO PODEM forma triângulo')