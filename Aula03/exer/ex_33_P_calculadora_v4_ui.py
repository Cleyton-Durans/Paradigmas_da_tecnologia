## PLP - Aula 3
## 13 mainov 2026
## Python - Calculadora Modular - versão 4


def mostrar_menu():
    print("\n=== CALCULADORA MODULAR v4===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

def ler_valores():
    while True:
        try:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            return x, y
        except ValueError:
            print("Entrada inválida! Digite apenas números.\n")
