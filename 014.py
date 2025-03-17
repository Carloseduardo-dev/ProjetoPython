#Escreva um progama qu converta uma temperatura digitada em  °C  e converta para °F.
temperatura_c = float(input('digite a temperatura °C :'))
conversor_temperatura = 9 * temperatura_c / 5
temperatura_f = 32 + conversor_temperatura
print(f'a temperatura {temperatura_c}°C equivale {temperatura_f}°F')
