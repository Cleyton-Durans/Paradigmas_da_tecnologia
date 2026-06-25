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


# --- Exemplo de uso ---
if __name__ == "__main__":
    estoque = Estoque()
    
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