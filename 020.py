#O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos.Faça um progama que leia o nome dos quatros alunos e mostre a ordem sorteada.
import random

input('Qual o nome do primeiro aluno :')
input('Qual o nome do segundo a aluno :')
input('Qual o nome do terceiro aaluno :')
input('Qual o nome do quarto aluno :')
ordem1 = ['cadu', 'mimi', 'anny', 'nanda'],['nanda', 'mimi', 'cadu', 'anny'],['mimi', 'anny', 'nanda', 'cadu']
print('-'*35)
print('A ORDEM DE APRESENTAÇÃO SERÁ :')
apresentacao = random.choice(ordem1)
print(apresentacao)
################################
n1 = str(input('Primeiro aluno :'))
n2 = str(input('Segundo aluno :'))
n3 = str(input('Terceiro aluno :'))
n4 = str(input('Quarto aluno :'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ORDEM DE APRESENTAÇÃO É:')
print(lista)