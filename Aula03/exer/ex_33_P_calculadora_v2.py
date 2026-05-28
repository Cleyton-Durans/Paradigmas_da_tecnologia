## PLP - Aula 3
## 13 mai 2026
## Python - Calculadora Modular - versão 2


def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Erro: divisão por zero não é permitida.")
        return None
    return a / b

# Programa principal
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

print(f"Soma = {soma(x, y)}")
print(f"Subtração = {subtrai(x, y)}")
print(f"Multiplicação = {multiplica(x, y)}")

resultado = divide(x, y)
if resultado is not None:
    print(f"Divisão = {resultado}")
