class Medico:
    def __init__(self,nome):
        self.nome = nome 

class Paciente:
    def __init__(self, nome):
        self.nome = nome

class Consulta:
    def __init__(self, medico,paciente):
        self.medico = medico
        self.paciente = paciente

medico = Medico ("Doutor JOÃO GABRIEL DE SÁ")
paciente = Paciente ("ANDREY")

consulta = Consulta (medico,paciente)

print(consulta.medico.nome)
print(consulta.paciente.nome)