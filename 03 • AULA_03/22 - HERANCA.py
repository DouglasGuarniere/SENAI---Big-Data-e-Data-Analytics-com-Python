class Animal():
    def __init__(self, nome, cor):
        self._nome = nome
        self._cor = cor
        
    def comer(self):
        print(f"0 {self._nome} está comendo!")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor) 

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)     

gato = Gato("Bichano","Branco")
cachorro = Cachorro("Totó","Preto") 
coelho = Coelho("Pernalonga","Cinza") 

gato.comer()
cachorro.comer()
coelho.comer()
