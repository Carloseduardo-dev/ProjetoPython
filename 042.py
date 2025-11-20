# #Desenvolva uma lógica que leia o peso de e altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com a tabela: -abaixo de 18.5: abaixo do peso, - entre 18.5 e 25: peso ideal, -De 25 até 30: sobrepeso, -De 30 até 40:obesidade, -acima de 40: obesidade móbida.

while True:
    try:
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        imc = peso / (altura **2)
        if imc < 18.5:
            print(f"Seu IMC é de: {imc:.2f} Kg sua categoria é abaixo do Peso!")
        elif imc <= 25:
            print(f"Seu IMC é de: {imc:.2f} Kg sua categoria é peso Ideal!")
        elif imc <= 30 :
            print(f"Seu IMC é de: {imc:.2f} Kg sua categoria é peso Sobrepeso!")
        elif imc <= 40 :
            print(f"Seu IMC é de: {imc:.2f} Kg sua categoria é peso Obesidade!")
        elif imc > 40:
            print(f"Seu IMC é de: {imc:.2f} Kg sua categoria é peso Obesidade Mórbida!")
    except:
       print("Use ponto [.] ao invés de Vírgula [,]!!!")
