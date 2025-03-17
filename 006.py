#Crie um algoritimo que leia um número e mostre o seu dobro , triplo e a raiz quadrada.
n = int(input('digite um número :'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('o dobro de {} vale {}.'.format(n, d))
print('o triplo de {} vale {}.'.format(n, t))
print('a raiz quadrada de {} vale {:.2f}'.format(n, r))
#raiz quadrada pode ser escrita dessa forma tbm:
pow(n, (1/2))

########################################################
a = int(input('digite um número:'))
r = pow(a, (1/2))
print('A raiz de {} vale {}'.format(a, r))
