#PROGAMA PARA MOSTRA FATORIAL DE UM NÚMERO USANDO LOOP WHILE E NO MESMO PROMAGA PERGUNTE AO USUÁRIO SE ELE QUER MOSTRAR MAIS TERMOS.O PROGAMA DEVE ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.
while True:
    numero = int(input('DIGITE UM NÚMERO E VEJA SEU FATORIAL:'))
    contador = numero
    fatorial = 1
    print(f'CALCULANDO {numero}! =', end=' ')
    while contador > 0:
        print(contador, end=' ')
        print('X' if contador > 1 else '=', end=' ')
        fatorial *= contador
        contador -= 1
    print(fatorial)
    resposta = str(input("QUER CONTINUAR [S- SIM] ou [N- NÃO]: ")).lower()
    if resposta == "n":
        print("FIM DO PROGAMA")
        break
    elif resposta == "s":
        continue
    else:
        print(f"VOCÊ DIGITOU [{resposta}] PROGAMA ENCERRADO POR CARACTER INVALIDO")
        break