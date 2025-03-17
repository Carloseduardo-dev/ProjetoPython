#Faça um progama que leia uma frase pelo teclado e mostre , Quantas vezes aparece a letra 'A'; Em que posição aparece pela 1° vez; Em que posião ela aparece pela última vez.
frase = str(input('Digite uma frase :')).lower().strip()
frase = frase.replace('ã','a')
print('quantidade de letra A, na frase')
print(frase.count('a'))
print('Primeira vez que aparece')
print(frase.find('a'))
print('Última vez que aparece :')
print(frase.rfind('a'))

