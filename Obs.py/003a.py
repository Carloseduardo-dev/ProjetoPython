#Manipulação de texto

frase = 'Curso Em Video Python'
#Fatiamento
print(frase[3])
print(frase[3:14])
print(frase[:14])
print(frase[:])
print(frase [:21:2])
print(frase[4::3])
print(frase[::5])
#count
print(frase.count('o'))
print(frase.upper().count('O'))
#len>>TAMANHO
print(len(frase))
#replace>>SUBSTITUIR
print(frase.replace('Python', 'Cadu'))
#in>>EM
print('Curso' in frase)
#find>>ENCONTRA
print(frase.find('Video'))
print(frase.lower().find('video'))
#upper>>AUMENTAR , lower>>DIMINUIR
print(frase.upper())
print(frase.lower())
#split>>DIVIDIR
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[3])
print(dividido[::3])
print(dividido[3:])
print(dividido[2][3])
