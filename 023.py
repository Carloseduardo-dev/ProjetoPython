#Faça um progama que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

#JEITO QUE FIZ
# num = int(input('Digite um número de 0 a 9999 :'))
# num = str(num)
# print('Esse número contém :')
# print('-'*30)
# print('Unidades:',(num[3:]))
# print('Dezenas:',(num[2]))
# print('Centenas:',(num[1]))
# print('milhar:',(num[0]))

#PROFESSOR
num = int(input('Digite um número entre 0 e 9999 :'))
unidade = num // 1 % 10
print('Unidade:',unidade)
dezena = num // 10 % 10
print('Dezena:',dezena)
centena = num // 100 % 10
print('Centena:',centena)
milhar = num // 1000 % 10
print('Milhar:',milhar)
