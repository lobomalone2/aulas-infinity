class Animal:

    def falar(self):
        print("Este animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late.")

class Gato(Animal):
    def falar(self):
        print("O gato mia.")

# Criando instâncias das classes

animal_generico = Animal()
cachorro = Cachorro()
gato = Gato()

# Chamando o método falar em cada instância

animal_generico.falar()
cachorro.falar()
gato.falar()