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
print(id(v))  # igual → mesma caixa, conteúdo mudou
