class Cliente:
    def __init__(self,nome):
        self.nome = nome
class Pedido:
    def __init__(self,nome):
        self.nome = nome
class Vendendor:
    def __init__(self,cliente,pedido):
        self.cliente = cliente
        self.pedido = pedido 

cliente = Cliente ("JOÃO GABRIEL")
pedido = Pedido ("PIZZA DE CARNE")

Vendendor = Vendendor (cliente, pedido)

print(Vendendor.cliente.nome)
print(Vendendor.pedido.nome)