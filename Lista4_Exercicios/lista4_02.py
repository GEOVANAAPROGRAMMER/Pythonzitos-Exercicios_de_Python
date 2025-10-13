nome = input("Digite seu nome: ")
senha = nome
while senha == nome:
    senha = input("Digite uma senha diferente do nome: ")
print("Senha cadastrada com sucesso!")