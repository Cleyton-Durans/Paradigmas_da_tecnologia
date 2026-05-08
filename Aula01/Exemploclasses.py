class Carro:
    rodas = 4 
    def __init__(self, marca):
        self.marca = marca

        def ligar(self):
            print(f"Oi, minha marca é {self.marca}")

c1 = Carro("Honda")

print("Chamando as instancia da classe.")
print(f" Marca --> {c1.marca}")
print(f" Rodas --> {c1.rodas}")
print("Chamando os atributos da classe.")
print(f" Rodas --> {Carro.rodas}")

