class Carro:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor

    def acelerar(self):
        print(f"O {self.marca} com motor {self.motor} está acelerando")

    def abastecer(self):
        print(f"O {self.marca} está sendo abastecido.")

carro1 = Carro("Toyota", "2.0")
carro2 = Carro("fusion", "2.1")

print(f"Carro 1: {carro1.marca} (Motor {carro1.motor})")
carro1.acelerar()
carro1.abastecer()

print(f"Carro 2: {carro2.marca} (Motor {carro2.motor})")
carro2.acelerar()
carro2.abastecer()