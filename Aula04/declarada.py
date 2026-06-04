# 5. Programação Declarativa
# Foca no o que quer, não em como fazer:

numeros = [1, 2, 3, 4, 5]
# Descreve o resultado desejado, não o processo
soma = sum(numeros)
print("A soma é:", soma)  # Saída: 15

# Exemplo com filter (declarativo):
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)  # Saída: [2, 4]
