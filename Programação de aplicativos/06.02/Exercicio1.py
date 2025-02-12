class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        "A cada ano, a pessoa envelhece e, se tiver menos de 21 anos, cresce 0,5 cm."
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5

    def engordar(self, kilos):
        "Aumenta o peso da pessoa."
        self.peso += kilos

    def emagrecer(self, kilos):
        "Diminui o peso da pessoa."
        self.peso -= kilos

    def crescer(self, cm):
        "Aumenta a altura da pessoa."
        self.altura += cm

pessoa1 = Pessoa("Anthony", 20, 70, 1.75)
print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade,"anos")
print("Peso:", pessoa1.peso,"kg")
print("Altura:", pessoa1.altura,"cm")

pessoa1.envelhecer()
print("Após envelhecer:")
print("Idade:", pessoa1.idade,"anos")
print("Altura:", pessoa1.altura,"cm")

pessoa1.engordar(2)
print("Após engordar:")
print("Peso:", pessoa1.peso,"kg")

pessoa1.emagrecer(3)
print("Após emagrecer:")
print("Peso:", pessoa1.peso,"kg")

pessoa1.crescer(0.5)
print("Após crescer:")
print("Altura:", pessoa1.altura,"cm")
