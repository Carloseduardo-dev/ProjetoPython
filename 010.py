#Crie um progama que leia quanto dinheiro uma pesssoa tem na carteira e mostre quantos dólares ela pode compra.(considere US$1.00=3.27 

valor = float(input('quantos reais você tem na carteira :R$'))
dollar = 5.94
conversor_dollar = valor / dollar
print('com {} R$ , você pode comprar {:.2f} US$'.format(valor, conversor_dollar))
