#Crie um progama que leia o nome completo de uma pessoa e mostre: nome com todas as letras maiúsculas, nome com todas as letras minúsculas, quantas letras ao todo sem considerar espaços, quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome :')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
dividido = nome.split()
print(len(dividido[0]))
