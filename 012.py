#Faça um algorítimo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto.
produto = float(input('qual valor do produto : R$'))
porcentagem = produto * 5 / 100
novo_preco = produto - porcentagem
print(f'nesse produto de R${produto:.2f} você receberá 5% de desconto e pagará apenas R${novo_preco:.2f} !')
