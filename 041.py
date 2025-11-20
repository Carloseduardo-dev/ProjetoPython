# A confederação Nacional de natação precisa de um progama que leia o ano de nascimento de um aluno atleta e mostre sua categoria, de acordo com a idade: -até 9 anos: Mirim, -até 14 anos: Infantil, -até 19 anos: Junior, - até 20 anos: Sênior, -acima Master.


anoAtual = int(input("Informe o ano que você está: "))
ano_atleta = int(input("Digite o ano de nascimento do atleta: "))
mediaIdade = anoAtual - ano_atleta
opcao = 0
while opcao != 3:
    print("=========================================================")
    opcao = int(input("DIGITE A OPÇÃO DESEJADA:\n[ 1 ] SABER SUA CATEGORIA\n[ 2 ] NOVO ATLETA\n[ 3 ] SAIR\n--> "))
    if opcao == 1:
        mediaIdade = anoAtual - ano_atleta
        if mediaIdade <= 9:
            print(f"Voçê possui {mediaIdade} anos e está na categoria Mirim")
        elif mediaIdade <= 14:
            print(f"Voçê possui {mediaIdade} anos e está na categoria Infântil")
        elif mediaIdade <= 19:
            print(f"Voçê possui {mediaIdade} anos e está na categoria Junior")
        elif mediaIdade <= 20:
            print(f"Voçê possui {mediaIdade} anos e está na categoria Sênior")
        elif mediaIdade > 20:
            print(f"Voçê possui {mediaIdade} anos e está na categoria Master")
    if opcao == 2:
        anoAtual = int(input("Informe o ano que você está: "))
        ano_atleta = int(input("Digite o ano de nascimento do atleta: "))
    if opcao == 3:
        print("FIM DO PROGAMA")

