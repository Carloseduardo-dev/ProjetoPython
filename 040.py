n1 = float(input('Qual a primeira nota do aluno:'))
n2 = float(input('Qual a segunda notado aluno:'))
media = (n1 + n2) / 2
if media < 5:
    print(f'Sua média foi {media}, você foi reprovado!')
elif media == 5 or media <= 6.999:
    print(f'Sua nota foi de {media},você foi para a recuperação!')
else:
    media >= 7
    print(f'Sua media foi {media}, você passou!')