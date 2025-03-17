#Escreva um progama que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('uma distâcia em metros : '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('a medida de {}m coresponde a\n{}dm \n{}cm \n{}mm'.format(medida, dm, cm, mm)) 

