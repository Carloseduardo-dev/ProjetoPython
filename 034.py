#Escreva um progama que pergunte o sálario de um funcionário e calcule o valor do seu aumento.Para salários superiores a 1250.00 calcule um aumento de 10%.Para os inferiores ou iguais ,o aumento é de 15%.

s = float(input('\033[7;35;40mDigite seu sálario:\033[m'))
if s <= 1250:
    aumento = s + (s * 15 / 100)
else:
    aumento = s + (s * 10 / 100)
print(f'\033[3;37;46mSeu novo salário será de {aumento}R$\033[m')
    