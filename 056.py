#Crie um progama que leia dois valores e mostre um menu na tela:
#[1]soma
#[2]multiplicar
#[3]maior
#[4]novos números
#[5]sair do progama
#seu progama deverá realizar a operação solicitada em cada
n1 = int(input('PRIMEIRO NÚMERO:'))
n2 = int(input('SEGUNDO NÚMERO:'))
opcao = 0
while opcao != 5:
    opcao = int(input('DIGITE A OPÇÃO DESEJADA:\n[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MOSTAR O MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR\n>>'))
    if opcao == 1:
        soma = n1 + n2
        print(f'SOMA ENTRE {n1} + {n2} É {soma}.')
    elif opcao == 2:
        produto = n1 * n2
        print(f'A MULTIPLICAÇÃO ENTRE {n1} X {n2} É {produto}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print( f'ENTRE {n1} e {n2} O MAIOR É {maior}')
        elif n2 > n1:
            maior = n2
            print( f'ENTRE {n1} e {n2} O MAIOR É {maior}')
        else:
            print(f'NÃO POSSUI UM NÚMERO MAIOR, OS DOIS SÃO IGUAIS: {n1} = {n2}')
    elif opcao == 4:
        n1 = int(input('PRIMEIRO NÚMERO:'))
        n2 = int(input('SEGUNDO NÚMERO:'))
    elif opcao == 5:
        print('FINALIZANDO')
    


