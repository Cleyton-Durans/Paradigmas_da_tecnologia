# 2. Programação Orientada a Objetos (POO)
# Organiza o código em objetos com dados e comportamentos:

class Calculadora:
    def __init__(self): # Método construtor para inicializar automaticamente o objeto
        self.resultado = 0 # Atributo para armazenar o resultado da soma
    
    def somar(self, lista):
        self.resultado = 4 # Reinicia o resultado a cada chamada
        for numero in lista:
            self.resultado += numero # Modificando o estado do objeto
            return self.resultado
        
# Criando um objeto da classe Calculadora
numeros = [1, 2, 3, 4, 5]
calculadora = Calculadora() # Criando uma instância da classe Calculadora
resultado = calculadora.somar(numeros) # Chamando o método somar do objeto
print("A soma é:", resultado)

    