#Escreva um progama que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar,sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.

carro = float(input('Qual a quantidade de KM rodados ?KM '))
aluguel =  float(input('Quantos dias foi alugado ?'))
dias = 60
km_rodado = 0.15
valor_aluguel = (carro * km_rodado) + (aluguel * dias)
print(f'o valor a ser pago pelo aluguel de {aluguel} dias será de R${valor_aluguel}')


