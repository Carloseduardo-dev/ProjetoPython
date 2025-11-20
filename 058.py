#CRIE UM PROGAMA QUE CALCULE O FATORIAL DE UM NÚMERO.USANDO O LOOP FOR.

n = int(input('FATORIAL: '))
f = 1
print(f'CALCULANDO {n}! =', end=' ')
for c in range(n, 0, -1):
    print(c, end=' ')
    print('X' if c > 1 else '=', end=' ')
    f *= c
print(f, end=' ')