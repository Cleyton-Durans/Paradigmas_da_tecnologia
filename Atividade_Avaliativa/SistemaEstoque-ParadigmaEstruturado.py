# Sistema de Gerenciamento de Estoque - Paradigma Estruturado (Simplificado)

estoque = []


def cadastrar_produto(nome, quantidade, preco):
    """Adiciona um produto ao estoque."""
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    print(f"Produto '{nome}' cadastrado!")


def vender_produto(nome, quantidade):
    """Atualiza o estoque após uma venda."""
    for produto in estoque:
        if produto["nome"] == nome:
            if produto["quantidade"] >= quantidade:
                produto["quantidade"] -= quantidade
                print(f"Venda de {quantidade} unidades de '{nome}'. Estoque atual: {produto['quantidade']}")
            else:
                print(f"Erro: Estoque insuficiente para '{nome}'.")
            return
    print(f"Erro: Produto '{nome}' não encontrado.")


def repor_produto(nome, quantidade):
    """Atualiza o estoque após uma reposição."""
    for produto in estoque:
        if produto["nome"] == nome:
            produto["quantidade"] += quantidade
            print(f"Reposição de {quantidade} unidades de '{nome}'. Estoque atual: {produto['quantidade']}")
            return
    print(f"Erro: Produto '{nome}' não encontrado.")


def calcular_valor_total():
    """Calcula o valor total do estoque."""
    total = sum(produto["quantidade"] * produto["preco"] for produto in estoque)
    return total


def produto_mais_caro():
    """Retorna o produto mais caro."""
    if not estoque:
        return None
    return max(estoque, key=lambda x: x["preco"])


def produto_mais_barato():
    """Retorna o produto mais barato."""
    if not estoque:
        return None
    return min(estoque, key=lambda x: x["preco"])


# --- Exemplo de uso ---
if __name__ == "__main__":
    # Cadastrar produtos
    cadastrar_produto("Arroz", 100, 5.99)
    cadastrar_produto("Feijão", 50, 8.50)
    cadastrar_produto("Açúcar", 200, 3.20)
    
    # Vender e repor
    vender_produto("Arroz", 10)
    repor_produto("Feijão", 20)
    
    # Calcular valor total
    print(f"Valor total do estoque: R${calcular_valor_total():.2f}")
    
    # Identificar produtos
    mais_caro = produto_mais_caro()
    mais_barato = produto_mais_barato()
    print(f"Produto mais caro: {mais_caro['nome']} (R${mais_caro['preco']:.2f})")
    print(f"Produto mais barato: {mais_barato['nome']} (R${mais_barato['preco']:.2f})")