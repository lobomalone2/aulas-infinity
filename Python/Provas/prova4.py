produtos = {}

for i in range(1,5):
    nome_produto = input(f'Digite o nome do produto{i + 1}:')
    preco_produto = float(input(f'Digite o preço do produto{i +1}'))


    produtos[nome_produto] = preco_produto

    total_compra = sum(produtos.values())
    print('\n Produtos e preços: ')


for produto, preco in produtos.items():

    print(f'{produto}: R$ {preco:.2f}')

    print(f'{produto}: R$ {preco:.2f}')

    print(f' \n Valor total da compra: R$ {total_compra:.2f}')