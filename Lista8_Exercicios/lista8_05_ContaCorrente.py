class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        # O self está dizendo que o atributo clientes que será recebido pertence ao atributo "clientes" da classe
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
    
    def resumo(self):
        print("CC Número: {} Saldo: {:.2f}".format(self.numero, self.saldo))
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(self.saldo)

    def depositar(self, valor):
        self.saldo += valor
        print(self.saldo)