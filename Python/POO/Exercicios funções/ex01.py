class Carro:
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def mostrar_detalhes(self):
        print(f'Carro: {self.marca}, {self.modelo}, Ano: {self.ano}, Cor: {self.cor}')



meu_carro = Carro("Toyota","Corolla", 2020,"Branco")

meu_carro.mostrar_detalhes()