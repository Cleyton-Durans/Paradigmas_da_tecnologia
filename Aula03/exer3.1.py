# PLP - Aula 2 - Exercício 3.1
#13 mai 2026 
# P - Escopo léxico

x = 10

def f():
    x = 20
    print(x)
    
f()
print(x)

