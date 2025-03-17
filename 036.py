#Escreva um progama para aprova o empréstimo bancário para a compra de uma casa. O progama vai pergunta o valor da casa, o sálario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal , sabendo que ela não pode exceder 30% do sálario ou então o emprestimo será negado.

# a = 1000
# b = a + (a * 30 / 100)
# c = a + 0.3 * a
# print(b)
# print(c)

casa = float(input('Qual o valor da casa:'))
s = float(input('Qual seu sálario:'))
anos = int(input('Quantos anos você irá pagar:'))
prestacao = casa / anos
print(f'Você irá pagar mensalmente {anos}  de prestações de {prestacao:.2f}R$')
s = s + 0.3 * s
prestacao = prestacao - 0,3 * prestacao
print(s)
