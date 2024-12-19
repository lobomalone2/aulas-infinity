class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def exibir_informacoes(self):
        print(f'Produto: {self.nome}, Preço: {self.preco}, Quantidade em estoque: {self.quantidade}')


Produto1 = Produto()

        