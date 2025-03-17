lista_vendas = [100, 5, 1000, 800, 35]
#pegar um item da lista
print(lista_vendas[0])#por exemplo 'item de numero 0'
#tamanho da lista, 'len'
qntde_vendas = len(lista_vendas)
print(qntde_vendas)
#somar todos os itens, 'sum'
total_vendas = sum(lista_vendas)
print(total_vendas)
#max, min, media
print(max(lista_vendas))
print(min(lista_vendas))
print(total_vendas / qntde_vendas)
#Encontrar um elemento 'in'(a posição do elemento)usando 'index'.
lista_produtos = ['iphone', 'ipad', 'aplle watch', 'airpod', 'macbook']
print('Airpod' in lista_produtos)
posicao = lista_produtos.index('airpod')
print(posicao)
pedaco_lista = lista_produtos[posicao:]
print(pedaco_lista)
#Editar um item
lista_precos = [5000, 7000, 3000, 1000, 10000]
novo_preco = lista_precos[0] * 1.1 #preço com 10% de aumento
lista_precos[0] = novo_preco
print(lista_precos)
#Remover um item da lista, 'remove'





