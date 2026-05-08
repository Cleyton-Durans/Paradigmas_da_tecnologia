"""Desafio:

 Crie uma classe Pessoa com atributos de instância nome e idade
 Adicione um método de instância que mostre nome e idade.
 Crie uma subclasse Aluno que herda de Pessoa e tenha um atributo adicional curso.
 Na classe Aluno, sobrescreva o método de instância para também mostrar o curso.
 Crie objetos de Pessoa e Aluno e teste os métodos.
 
 """

class Pessoa:
    def __init__(self,nome,idade,):
        self.nome = nome
        self.idade = idade

    def mostrardados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}") 
            

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, matricula):
         super().__init__(nome, idade)
         self.curso = curso
         self.matricula = matricula

    def mostrarcurso(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Curso: {self.curso}")
        print(f"Matricula: {self.matricula}")


a1 = Pessoa("Durans", 25)
a2 = Aluno("Durans", 25, "Pyhton", 125444)

a1 .mostrardados()
print("______")
a2 .mostrarcurso()





         
    