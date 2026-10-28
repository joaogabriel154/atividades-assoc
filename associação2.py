class Professor:
   def __init__(self,nome):
     self.nome = nome

class Turma:
    def __init__(self, nome):
       self.nome = nome 

class Disciplina:
    def __init__(self, professor, turma):
       self.professor = professor
       self.turma = turma

professor = Professor ("JOÃO GABRIEL")
turma = Turma ("2° Ano DS")

disciplina = Disciplina (professor,turma)

print(disciplina.professor.nome)
print(disciplina.turma.nome)