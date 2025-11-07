from lista8_05_ContaCorrente import Conta
from lista8_05_ContaCorrente import Cliente

Maria = Cliente("Maria", "9999-9999")
João = Cliente("João", "8888-8888")

print("Nome: {} Telefone: {}".format(Maria.nome, Maria.telefone))
print("Nome: {} Telefone: {}".format(João.nome, João.telefone))

conta1 = Conta([Maria], 1234, 10000)
conta2 = Conta([João, Maria], 5678, 500)

print("Conta 1:" )
conta1.resumo()
print("Conta 2:" )
conta2.resumo()