#CRIE UM PROGAMA QUE CALCULE O FATORIAL DE UM NÚMERO.USANDO O LOOP WHILE.

n = int(input('DIGITE UM NÚMERO E VEJA SEU FATORIAL:'))
c = n
f = 1
print(f'CALCULANDO {n}! =', end=' ')
while c > 0:
    print(c, end=' ')
    print('X' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)