ano = float(input('Qual seu ano de nascimento:'))
ano_atual = float(input('Qual seu ano atual:'))
alistamento = 18
idade = ano_atual - ano
if idade > alistamento:
    print(f'Você está com {idade} anos,ja passou {idade - alistamento} do tempo de se alistar!')
elif idade == alistamento:
    print('Esta na hora de se alistar!')
else:
    print(f'Você esta com {idade} anos,ainda não é o momento de se alistar,faltam {alistamento - idade} anos!')
