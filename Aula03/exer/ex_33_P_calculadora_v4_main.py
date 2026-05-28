## PLP - Aula 3
## 07 nov 2025
## Python - Calculadora Modular - versão 4


import ex_33_P_calculadora_v4_ui as ui
import ex_33_P_calculadora_v4_ops as ops

def main():
    while True:
        ui.mostrar_menu()
        opcao = input("Escolha a operação: ")

        if opcao == "0":
            print("Encerrando o programa...")
            break

        # Verifica se a opção é válida antes de pedir os números
        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida! Tente novamente.\n")
            continue  # volta ao início do laço sem pedir números

        # Só pede os números se a opção for válida
        x, y = ui.ler_valores()

        if opcao == "1":
            print(f"Resultado: {ops.soma(x, y)}")
        elif opcao == "2":
            print(f"Resultado: {ops.subtrai(x, y)}")
        elif opcao == "3":
            print(f"Resultado: {ops.multiplica(x, y)}")
        elif opcao == "4":
            r = ops.divide(x, y)
            if r is not None:
                print(f"Resultado: {r}")

if __name__ == "__main__":
    main()
 