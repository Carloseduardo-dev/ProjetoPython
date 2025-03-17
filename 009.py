#Faça um progama que leia um numero inteiro qualquer e mostre na tela sua tabuada.

num = int(input('digite um número e veja sua tabuada:'))
num1 = num * 1
num2 = num * 2
num3 = num * 3
num4 = num * 4
num5 = num * 5
num6 = num * 6
num7 = num * 7
num8 = num * 8
num9 = num * 9
num10 = num * 10
print('{} x 1 ={:2}\n{} x 2 ={:2}\n{} x 3 ={:2}\n{} x 4 ={:2}\n{} x 5 ={:2}\n{} x 6 ={:2}\n{} x 7 ={:2}\n{} x 8 ={:2}\n{} x 9 ={:2}\n{} x 10={:2}'.format(num, num1, num, num2, num, num3, num, num4, num, num5, num, num6, num, num7, num, num8, num, num9, num, num10,)) 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
num = int(input('digite um número e veja sua tabuada :'))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))