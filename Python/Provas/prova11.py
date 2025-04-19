class Veiculo:

    def __init__(self):
        pass

    def movimentar(self):

        print('O veículo esta em movimento')

class Carro(Veiculo):

    def movimentar(self):

        print ("Carro está dirigindo")
    
class Moto(Veiculo):

    def movimentar(self):

        print("Moto está acelerando" )

veiculo = Veiculo()
carro = Carro()
moto = Moto()

veiculo.movimentar()
carro.movimentar()
moto.movimentar()



