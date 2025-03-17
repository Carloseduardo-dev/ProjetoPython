#Faça um algorítimo que leia o sálario de um funcionário e mostre seu novo sálario ,com 15% de aumento.

salario = float(input('Digite seu sálario :R$'))
porcentagem = salario * 15 / 100
novo_salario = salario + porcentagem
print(f'Seu sálario de {salario}R$ passará a ser de R${novo_salario:.2f} com o aumento de 15% !')
