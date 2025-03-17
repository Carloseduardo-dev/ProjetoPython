#Desenvolva um progam que pergunte a distância de uma viagem em Km. Calcule o preço da passagem . Cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.

viagem = int(input('Qual a distância da sua viagem ? Km '))    
#Se a viagem não for maior que 20km aconte isso:   
if viagem == 200 :
    taxa1 = 0.5 * 200
    print(f'Sua viagem foi de {viagem}Km e o valor da passagem foi de {taxa1}R$')
#Se for maior que 200Km acontece isso:
else :
    taxa2 = viagem * 0.45
    print(f'Sua viagem foi de {viagem}km e o valor da passagem foi de {taxa2}R$')

