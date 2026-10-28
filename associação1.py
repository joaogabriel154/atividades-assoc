class Aluno:
   def __init__(self, nome):
    self.nome = nome 

class Equipamento:
   def __init__(self, nome):
    self.nome = nome 

class Emprestimo:
    def __init__(self, aluno , equipamento):
     self.aluno = aluno
     self.Equipamento = equipamento

aluno1 = Aluno ("JOÃO GABRIEL")
notbook =  Equipamento("notebook dell")

emprestimo = Emprestimo(aluno1, notebook)


print(emprestimo.aluno.nome)
print(emprestimo.equipamento.nome)
