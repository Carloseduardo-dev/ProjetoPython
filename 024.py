#Crie um progama que leia o nome de uma cidade e diga se ela começa ou não com o nome'SANTO'.

cidade = str(input('Digite o nome de uma cidade :')).strip()
print('Começa com santo?')
print(cidade[:5].upper) == 'SANTO'
