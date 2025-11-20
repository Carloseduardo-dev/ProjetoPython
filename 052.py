anoAtual = 2025
maior = 0
menor = 0
for p in range(1, 7):
    print(f'{p}º PESSOA:')
    ano = int(input('Seu ano de nascimento: '))
    idade = anoAtual - ano
    print(f'{idade} anos')
    if idade >= 18:
        maior += 1
    if idade <= 17:
        menor += 1
print(f'{maior} pessoas, Já são maiores de idade!')
print(f'{menor} pessoas, São menores de idade!')
        