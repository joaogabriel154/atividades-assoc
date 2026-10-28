class Produto:
    def __init__(self, nome, preco, estoque):
        self._nome = nome
        self._preco = preco
        self._estoque = estoque

    @property
    def estoque(self):
        return self._estoque

    def vender_item(self, quantidade):
        if quantidade <= self.estoque:
            self._estoque -= quantidade
            return True
        return False

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Venda:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        if produto.vender_item(quantidade):
            self.itens.append((produto._nome, quantidade))
            print(f"Sucesso: {quantidade}x {produto._nome} adicionado(s) à venda.")
        else:
            print(f"Erro: Estoque insuficiente para {produto._nome}.")

cliente1 = Cliente("joão gabriel", "062.522.982-11")
macarrão = Produto("macarrão", 11.00, 10)

venda = Venda(cliente1)
venda.adicionar_produto(macarrão, 2)
venda.adicionar_produto(macarrão, 4)

print(f"estoque final do notebook: {macarrão.estoque}")