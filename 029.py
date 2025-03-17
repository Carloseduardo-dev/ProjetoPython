#Escreva um progama que leia a velocidade de um carro. Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada km acima do limite.
 
velocidade = float(input('qual velocidade do carro:km '))

if velocidade > 80 :
    print('MULTADO! você excedeu o limite de velocidade que é de 80Km/h')
    multa = (velocidade - 80 ) * 7.00
    print(f'Valor da multa {multa}R$')
print('Tenha um bom dia, diriga com segurança !')   
    
    
    
    