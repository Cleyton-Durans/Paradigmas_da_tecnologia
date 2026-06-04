#   4. Programação Estruturada
#   Usa apenas sequência, decisão e repetição (sem goto):

numeros = [1, 2, 3, 4, 5]
soma = 0
i = 0

while i < len(numeros):
    if numeros[i] > 0:
        soma += numeros[i]
    
    i += 1
    print(f"Adicionando o {numeros[i]} a soma: {soma}")
    
