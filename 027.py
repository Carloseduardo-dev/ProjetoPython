#Faça um progama que leia o nome completo de uma pessoa, mostando o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome :')).strip()
nome = nome.split()
print('Primeiro nome :')
primeiro = nome[0]
print(primeiro)
print('Último nome :')
ultimo = nome[-1]
print(ultimo)