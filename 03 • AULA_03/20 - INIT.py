class Pessoa:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

NovaPessoa = Pessoa("Joao","15")

print(NovaPessoa.nome)
print(NovaPessoa.idade)
