class Pessoa:
    def __init__(self,nome,idade,idioma):
        self.nome = nome
        self.idade = idade
        self.idioma = idioma

    def apresentar(self):
        print(f'oi, meu nome é: {self.nome}, tenho {self.idade} anos e estou aprendendo {self.idioma}')


pessoa1 = Pessoa('Ana',25,'inglês')
pessoa2 = Pessoa('Carlos',30,'Espanhol')

pessoa1.apresentar()
pessoa2.apresentar()