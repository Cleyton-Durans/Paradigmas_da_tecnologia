# Sistema de Gerenciamento de Estoque Orientado a Objetos
# Este código implementa um sistema de gerenciamento de estoque utilizando o paradigma de programação orientada a objetos. 
# Ele define classes para representar produtos e o estoque, 
# permitindo cadastrar produtos, atualizar o estoque, calcular valores totais e identificar produtos mais caros ou baratos.

#Class Produto representa um produto no estoque.
class Produto:  
    def __init__(self, nome, quantidade, preco):    
        self.nome = nome
        self.quantidade = quantidade  
        self.preco = preco    

    def __repr__(self):
        return f"Produto(nome :'{self.nome}', quantidade :{self.quantidade}, preco : R${self.preco})"
    
    # Encapsulamento dos atributos com propriedades para garantir a integridade dos dados.
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O nome do produto deve ser uma string não vazia.")
        self._nome = novo_nome
        
    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if not isinstance(nova_quantidade, int) or nova_quantidade < 0:
            raise ValueError("A quantidade deve ser um número inteiro não negativo.")
        self._quantidade = nova_quantidade

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if not isinstance(novo_preco, (int, float)) or novo_preco < 0:
            raise ValueError("O preço deve ser um número não negativo.")
        self._preco = novo_preco

#Class ProdutoPerecivel herda da classe Produto e adiciona o atributo data_validade
class ProdutoPerecivel(Produto):
    def __init__(self, nome, quantidade, preco, data_validade):
        super().__init__(nome, quantidade, preco)
        self.data_validade = data_validade
        
    @property
    def data_validade(self) -> str:
        return self._data_validade

    @data_validade.setter
    def data_validade(self, nova_data: str):
        if not isinstance(nova_data, str) or not nova_data.strip():
            raise ValueError("A data de validade deve ser uma string não vazia.")
        self._data_validade = nova_data

#Inicio da Class Estoque
class Estoque:
    def __init__(self):
        self.produtos = []
    # Cadastrar um novo produto no estoque utilizando a classe Produto
    # Try e except para capturar erros de entrada e garantir que os dados sejam válidos.
    # Método verifica se o produto já existe no estoque antes de adicioná-lo.
    def cadastrar_produto(self, nome, quantidade, preco):
        try:
            for p in self.produtos:
                if p.nome.lower() == nome.lower():
                    print(f"Produto '{nome}' já cadastrado!")
                    return
            produto = Produto(nome, quantidade, preco)
            self.produtos.append(produto)
            print(f"Produto '{nome}' cadastrado com sucesso!")
        except ValueError as e: print(f"Erro ao cadastrar produto: {e}")
    # Método para atualizar o estoque, seja para venda ou reposição.
    # try e except para capturar erros de entrada e garantir que os dados sejam válidos.    
    def atualizar_estoque(self, nome, quantidade, operacao="venda"):
        try:
            if not isinstance(quantidade, int) or quantidade < 0:
                raise ValueError("A quantidade deve ser um número inteiro não negativo.")
            for produto in self.produtos:
                if produto.nome.lower() == nome.lower():
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
        except ValueError as e: print(f"Erro ao atualizar estoque: {e}")
   
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
                valor_total = produto.quantidade * produto.preco
                print(f"{produto.nome}: {produto.quantidade} unidades - R${produto.preco:.2f} (Valor total: R${valor_total:.2f})")
            print("---------------------------") 
                    
    def mostrar_valor_individual(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                print(f"Valor individual de '{produto.nome}': R${produto.preco:.2f}")
                return
        print(f"Produto '{nome}' não encontrado.")
# Função menu para interação com o usuário, permitindo cadastrar produtos, atualizar estoque, calcular valores e listar produtos.
# A função utiliza um loop while para manter o menu ativo até que o usuário decida sair.
def menu(): 
    estoque = Estoque() 
    
    # Cadastrando produto manualmente
    estoque.cadastrar_produto("Arroz", 10, 20.99)
    estoque.cadastrar_produto("cafe", 5, 29.99)
    estoque.cadastrar_produto("feijao", 3, 11.99)
    estoque.cadastrar_produto("leite", 2, 3.99)

    while True:
        print("\n--- Sistema de Gerenciamento de Estoque ---")
        print("1. Cadastrar produto")
        print("2. Atualizar estoque (venda/reposição)")
        print("3. Calcular valor total do estoque")
        print("4. Mostrar valor individual de um produto")  # Opção alterada
        print("5. Identificar produto mais barato")
        print("6. Listar todos os produtos")
        print("0. Sair")

        try:
            opcao = input("Escolha uma opção: ").strip()

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
                nome = input("Digite o nome do produto: ")
                estoque.mostrar_valor_individual(nome)  # Chamada corrigida

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

        except ValueError as e:
            print(f"Erro de entrada: {e}. Por favor, insira valores válidos.")
            
if __name__ == "__main__":
    menu()