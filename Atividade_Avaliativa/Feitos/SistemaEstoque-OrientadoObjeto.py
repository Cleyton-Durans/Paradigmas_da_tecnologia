class Produto:  
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __repr__(self):
        return f"Produto(nome='{self.nome}', quantidade={self.quantidade}, preco={self.preco})"


class Estoque:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, nome, quantidade, preco):
        produto = Produto(nome, quantidade, preco)
        self.produtos.append(produto)
        print(f"Produto '{nome}' cadastrado com sucesso!")

    def atualizar_estoque(self, nome, quantidade, operacao="venda"):
        for produto in self.produtos:
            if produto.nome == nome:
                if operacao == "venda":
                    if produto.quantidade >= quantidade:
                        produto.quantidade -= quantidade
                    else:
                        print(f"Erro: Quantidade insuficiente de '{nome}' para vender.")
                        return
                elif operacao == "reposicao":
                    produto.quantidade += quantidade
                print(f"Estoque de '{nome}' atualizado. Nova quantidade: {produto.quantidade}")
                return
        print(f"Produto '{nome}' não encontrado!")

    def calcular_valor_total_estoque(self):
        total = sum(produto.quantidade * produto.preco for produto in self.produtos)
        return total

    def identificar_produto_mais_caro(self):
        if not self.produtos:
            return None
        return max(self.produtos, key=lambda x: x.preco)

    def identificar_produto_mais_barato(self):
        if not self.produtos:
            return None
        return min(self.produtos, key=lambda x: x.preco)

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("--- Produtos no Estoque ---")
            for produto in self.produtos:
                print(f"{produto.nome}: {produto.quantidade} unidades - R${produto.preco:.2f}")


# --- Menu Interativo ---
def menu(): 
    estoque = Estoque() 
    
    # Cadastrando produto manualmente
    estoque.cadastrar_produto("Arroz", 10, 20.99)
    estoque.cadastrar_produto("cafe", 5, 29.99)
    estoque.cadastrar_produto("feijao", 3, 11.99)
    estoque.cadastrar_produto("leite", 2, 3.99)
    estoque.cadastrar_produto("arroz", 4, 19.99)
    
    while True:
        print("\n--- Sistema de Gerenciamento de Estoque ---")
        print("1. Cadastrar produto")
        print("2. Atualizar estoque (venda/reposição)")
        print("3. Calcular valor total do estoque")
        print("4. Identificar produto mais caro")
        print("5. Identificar produto mais barato")
        print("6. Listar todos os produtos")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: R$"))
            estoque.cadastrar_produto(nome, quantidade, preco)

        elif opcao == "2":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            operacao = input("Operação (venda/reposicao): ").lower()
            estoque.atualizar_estoque(nome, quantidade, operacao)

        elif opcao == "3":
            total = estoque.calcular_valor_total_estoque()
            print(f"Valor total do estoque: R${total:.2f}")

        elif opcao == "4":
            mais_caro = estoque.identificar_produto_mais_caro()
            if mais_caro:
                print(f"Produto mais caro: {mais_caro.nome} (R${mais_caro.preco:.2f})")
            else:
                print("Nenhum produto cadastrado.")

        elif opcao == "5":
            mais_barato = estoque.identificar_produto_mais_barato()
            if mais_barato:
                print(f"Produto mais barato: {mais_barato.nome} (R${mais_barato.preco:.2f})")
            else:
                print("Nenhum produto cadastrado.")

        elif opcao == "6":
            estoque.listar_produtos()

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()