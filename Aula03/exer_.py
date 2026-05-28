## PLP - Aula 3
## 13 mai 2026
## P - Conteúdo variáveis
 
# Imutável (int)
x = 10
print(id(x))
x += 1
print(id(x))  # mudou → nova caixa
 
# Mutável (lista)
v = [1, 2, 3]
print(id(v))
v.append(4)
print(id(v))  # igual a mesma caixa, conteudo mudou

"""variáveis inteiras, float, str e etc, são como se fossem "únicas" e só podem ser guardadas em uma única gaveta exclusiva só delas.
você não consegue mudar essa variável e guardar de novo na mesma gaveta, tem que colocar em uma gaveta nova (gerando um novo ID) 
Já uma lista, por exemplo, eu guardo ela em uma gaveta, e qualquer mudança vai ser guardada na mesma gaveta que já existe. (mantendo o mesmo ID)
"""