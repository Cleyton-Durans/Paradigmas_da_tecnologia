# ==========================================================
# EXERCÍCIO GUIADO - PYTHON
# Leitura de nome e número inteiro
# Classificação do número como positivo, negativo ou zero
# ==========================================================

# Entrada de dados
nome = input("Digite seu nome: ")
numero = int(input("Digite um número inteiro: "))

# Processamento e saída
if numero > 0:
    print(nome + ", o número digitado é positivo.")
elif numero < 0:
    print(nome + ", o número digitado é negativo.")
else:
    print(nome + ", o número digitado é zero.")