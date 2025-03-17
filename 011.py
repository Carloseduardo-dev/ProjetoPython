#Faça um progama que leia a largura e a altura de uma parede em metros , calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('digite a largura : '))
altura = float(input('digite a altura : '))
area = altura * largura
litro_tinta = area / 2

print(f'Para pintar essa parede de {largura}X{altura} de dimenssão e área igual a {area}m² você precisará de {litro_tinta} litros de tinta !')