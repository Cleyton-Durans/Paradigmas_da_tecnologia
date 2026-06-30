
from functools import reduce

produtos = []

def valor_total_produto(produto):
    return produto["preco"] * produto["quantidade"]


def produto_mais_caro(lista):
    if len(lista) == 1:
        return lista[0]

    maior = produto_mais_caro(lista[1:])

    return lista[0] if lista[0]["preco"] > maior["preco"] else maior


def produto_mais_barato(lista):
    if len(lista) == 1:
        return lista[0]

    menor = produto_mais_barato(lista[1:])

    return lista[0] if lista[0]["preco"] < menor["preco"] else menor


while True:

    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Mostrar valor individual dos produtos")
    print("3 - Mostrar produtos sem estoque")
    print("4 - Mostrar produtos acima de um valor")
    print("5 - Mostrar valor total do estoque")
    print("6 - Mostrar produto mais caro")
    print("7 - Mostrar produto mais barato")
    print("8 - Ordenar produtos por preço")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))

        produtos.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        })

        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        valores = list(map(lambda p: p["preco"], produtos))

        print("\nVALOR INDIVIDUAL DOS PRODUTOS")
        for produto, valor in zip(produtos, valores):
            print(f"{produto['nome']}: R$ {valor:.2f}")

    elif opcao == "3":
        sem_estoque = list(filter(lambda p: p["quantidade"] == 0, produtos))

        print("\nPRODUTOS SEM ESTOQUE")
        for produto in sem_estoque:
            print(produto["nome"])

    elif opcao == "4":
        valor = float(input("Mostrar produtos acima de R$ "))

        resultado = list(filter(lambda p: p["preco"] > valor, produtos))

        print("\nPRODUTOS ENCONTRADOS")
        for produto in resultado:
            print(f"{produto['nome']} - R$ {produto['preco']:.2f}")

    elif opcao == "5":
        total = reduce(
            lambda soma, produto: soma + valor_total_produto(produto),
            produtos,
            0
        )

        print(f"\nValor total do estoque: R$ {total:.2f}")

    elif opcao == "6":
        if produtos:
            caro = produto_mais_caro(produtos)
            print(f"\nProduto mais caro: {caro['nome']} - R$ {caro['preco']:.2f}")
        else:
            print("Nenhum produto cadastrado.")

    elif opcao == "7":
        if produtos:
            barato = produto_mais_barato(produtos)
            print(f"\nProduto mais barato: {barato['nome']} - R$ {barato['preco']:.2f}")
        else:
            print("Nenhum produto cadastrado.")

    elif opcao == "8":
        ordenados = sorted(produtos, key=lambda p: p["preco"])

        print("\nPRODUTOS ORDENADOS POR PREÇO")
        for produto in ordenados:
            print(f"{produto['nome']} - R$ {produto['preco']:.2f}")

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")