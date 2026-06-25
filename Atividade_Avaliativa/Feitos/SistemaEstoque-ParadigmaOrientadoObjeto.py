# Sistema de Gerenciamento de Estoque - Paradigma Orientado a Objetos (Simplificado)

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def calcular_valor_total(self):
        return self.quantidade * self.preco


class Estoque:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, nome, quantidade, preco):
        """Adiciona um produto ao estoque."""
        self.produtos.append(Produto(nome, quantidade, preco))
        print(f"Produto '{nome}' cadastrado!")

    def vender_produto(self, nome, quantidade):
        """Atualiza o estoque após uma venda."""
        for produto in self.produtos:
            if produto.nome == nome:
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                    print(f"Venda de {quantidade} unidades de '{nome}'. Estoque atual: {produto.quantidade}")
                else:
                    print(f"Erro: Estoque insuficiente para '{nome}'.")
                return
        print(f"Erro: Produto '{nome}' não encontrado.")

    def repor_produto(self, nome, quantidade):
        """Atualiza o estoque após uma reposição."""
        for produto in self.produtos:
            if produto.nome == nome:
                produto.quantidade += quantidade
                print(f"Reposição de {quantidade} unidades de '{nome}'. Estoque atual: {produto.quantidade}")
                return
        print(f"Erro: Produto '{nome}' não encontrado.")

    def calcular_valor_total(self):
        """Calcula o valor total do estoque."""
        return sum(produto.calcular_valor_total() for produto in self.produtos)

    def produto_mais_caro(self):
        """Retorna o produto mais caro."""
        if not self.produtos:
            return None
        return max(self.produtos, key=lambda x: x.preco)

    def produto_mais_barato(self):
        """Retorna o produto mais barato."""
        if not self.produtos:
            return None
        return min(self.produtos, key=lambda x: x.preco)

def menu():
    estoque = Estoque()
    
    """
    # Cadastrar produtos
    estoque.cadastrar_produto("Arroz", 100, 5.99)
    estoque.cadastrar_produto("Feijão", 50, 8.50)
    estoque.cadastrar_produto("Açúcar", 200, 3.20)
    
    # Vender e repor
    estoque.vender_produto("Arroz", 10)
    estoque.repor_produto("Feijão", 20)
    
    # Calcular valor total
    print(f"Valor total do estoque: R${estoque.calcular_valor_total():.2f}")
    
    # Identificar produtos
    mais_caro = estoque.produto_mais_caro()
    mais_barato = estoque.produto_mais_barato()
    print(f"Produto mais caro: {mais_caro.nome} (R${mais_caro.preco:.2f})")
    print(f"Produto mais barato: {mais_barato.nome} (R${mais_barato.preco:.2f})")
    """
    
    while True:
        print("\n===== SISTEMA DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Vender produto")
        print("3 - Repor produto")
        print("4 - Mostrar valor individual dos produtos")
        print("5 - Mostrar produtos sem estoque")
        print("6 - Mostrar produtos acima de um valor")
        print("7 - Mostrar valor total do estoque")
        print("8 - Mostrar produto mais caro")
        print("9 - Mostrar produto mais barato")
        print("10 - Ordenar produtos por preço")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: R$"))
            estoque.cadastrar_produto(nome, quantidade, preco)

        elif opcao == "2":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a vender: "))
            estoque.vender_produto(nome, quantidade)

        elif opcao == "3":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a repor: "))
            estoque.repor_produto(nome, quantidade)

        elif opcao == "4":
            estoque.mostrar_valor_individual()

        elif opcao == "5":
            estoque.mostrar_produtos_sem_estoque()

        elif opcao == "6":
            valor_minimo = float(input("Valor mínimo (R$): "))
            estoque.mostrar_produtos_acima_de_valor(valor_minimo)

        elif opcao == "7":
            print(f"Valor total do estoque: R${estoque.calcular_valor_total():.2f}")

        elif opcao == "8":
            mais_caro = estoque.produto_mais_caro()
            if mais_caro:
                print(f"Produto mais caro: {mais_caro.nome} (R${mais_caro.preco:.2f})")
            else:
                print("Não há produtos cadastrados.")

        elif opcao == "9":
            mais_barato = estoque.produto_mais_barato()
            if mais_barato:
                print(f"Produto mais barato: {mais_barato.nome} (R${mais_barato.preco:.2f})")
            else:
                print("Não há produtos cadastrados.")

        elif opcao == "10":
            produtos_ordenados = estoque.ordenar_produtos_por_preco()
            print("Produtos ordenados por preço (crescente):")
            for produto in produtos_ordenados:
                print(f"{produto.nome} (R${produto.preco:.2f})")

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()