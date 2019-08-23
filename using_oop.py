class Animal:
    def __init__(self, nome, anos, qtd_patas):
        self.nome = nome
        self.anos = anos
        self.qtd_patas = qtd_patas
    def som(self, som, nome):
        print(nome, ": ", self.som)
        
class Pato(Animal):
    som = "Quack!"
    
class Papagaio(Animal):
    som = "Curupapo!"

class Cachorro(Animal):
    som = "AU AU!"

class Cobra(Animal):
    som = "Sssssss... Python é legal!"

pato = Pato("Antônia", "2", "2")
papagaio = Papagaio("José", "15", "2")
cachorro = Cachorro("Ringo", "5", "4")
cobra = Cobra("Python", "39", "0")

print("O nome dele(a) é", pato.nome, ", tem",pato.anos,"anos de idade e tem",pato.qtd_patas,"pernas.")
print(pato.som, "\n")

print("O nome dele(a) é", papagaio.nome, ", tem",papagaio.anos,"anos de idade e tem",papagaio.qtd_patas,"pernas.")
print(papagaio.som, "\n")

print("O nome dele(a) é", cachorro.nome, ", tem",cachorro.anos,"anos de idade e tem",cachorro.qtd_patas,"pernas.")
print(cachorro.som, "\n")

print("O nome dele(a) é", cobra.nome, ", tem",cobra.anos,"anos de idade e tem",cobra.qtd_patas,"pernas.")
print(cobra.som, "\n")
