#Desenvolva um progama que leia nome, idade, e sexo de 4 pessoas, No final do progama mostre: Média de idade do grupo, Qual o nome do homem mais velho, Quantas mulheres tem menos de 20 anos.
# con = 0
# ac = 0
# for p in range(3):
#     n = str(input("Qual seu nome: "))
#     id = int(input("Qual sua idade: "))
#     s = str(input("Qual seu sexo: "))
#     con += id
#     ac += 1
#     media = con / ac
# print(f'A média de idade é de {media:.2f} anos!')
# maior = 18
# while s == 'M' or 'm':
#     homem = 'homem'
#     if homem > maior:
#         print(homem)   
#     break
somaIdade = 0
acumIdade = 0 
maioridadehomem = 0
nomevelho = ''
mulhermenos20 = 0
for pessoa in range(1, 5):
    print(f'>>>{pessoa}º PESSOA <<<')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: '))
    somaIdade += idade
    acumIdade += 1 
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenos20 += 1
print(f'O homem mais velho se chama {nomevelho} e possui {maioridadehomem} anos')
print(f'A média de idade foi de {somaIdade / acumIdade} anos')
print(f'Ao todo são {mulhermenos20} mulheres com menos de 20 anos')



    





