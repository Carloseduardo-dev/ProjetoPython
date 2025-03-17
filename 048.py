soma = 0
cont = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
                #Acumulador(vai acumulando os valores seja ele somando ou multiplicando.)
                soma += c
                #Contador normalmente soma +1 ou seja soma 1 do valor anterior.
                cont += 1
print(soma)
print(cont)      