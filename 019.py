#Um professor quer sortear um dos seus quatro alunos para apagar o quadro .Faça um progama que ajude ele,lendo o nome deles e escrevendo o nome do escolhido.
import random

input('Digite o nome do primeiro aluno :')
input('Digite o nome do segundo aluno :')
input('Digite o nome do terceiro aluno :')
input('Digite o noome do quarto aluno :')
lista_alunos = ['cadu','nanda','mimi','anny']
sorteio = random.choice(lista_alunos)
print('O ALUNO QUE IRÁ APAGAR O QUADRO É :')
print('='*30)
print(sorteio)
################jeito do professor####################
n1 = str(input('Primeiro aluno :'))
n2 = str(input('Segundo aluno :'))
n3 = str(input('Terceiro aluno :'))
n4 = str(input('Quarto aluno :'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O ALUNO SORTEADO FOI :')
print(escolhido)