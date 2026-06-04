""" Função recursiva de 5 a 0"""

def contagem_regressiva(n):
    print(n)
    if n > 0:
        print(f'Chamando a função novamente com número = {n - 1}')
        contagem_regressiva(n - 1)
    else:
        print("A função não será chamada novamente, pois n é igual a 0.")
        
# Chamando a função com o valor inicial de 5
contagem_regressiva(5)
