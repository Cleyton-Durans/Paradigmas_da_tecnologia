## PLP - Aula 3
## 13 mai nov 2026
## Python - Calculadora Modular - versão 3


def soma(a, b): return a + b
def subtrai(a, b): return a - b
def multiplica(a, b): return a * b
def divide(a, b):
    if b == 0:
        print("Erro: divisão por zero.")
        return None
    return a / b

while True:
    print("\n=== CALCULADORA v3===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = input("Escolha a operação: ")

    if opcao == "0":
        print("Encerrando...")
        break

    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    if opcao == "1":
        print(f"Resultado: {soma(x, y)}")
    elif opcao == "2":
        print(f"Resultado: {subtrai(x, y)}")
    elif opcao == "3":
        print(f"Resultado: {multiplica(x, y)}")
    elif opcao == "4":
        r = divide(x, y)
        if r is not None:
            print(f"Resultado: {r}")
    else:
        print("Opção inválida! Tente novamente.")

