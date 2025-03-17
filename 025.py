#Crie um progama que leia o nome de uma pessoa e diga se ela tem 'silva' no nome.

nome = str(input('Digite seu nome :')).strip()
print('Seu nome tem Silva ?')
print('SILVA' in nome.upper())