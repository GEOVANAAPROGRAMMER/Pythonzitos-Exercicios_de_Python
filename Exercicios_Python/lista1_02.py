# 2. Faça um programa que leia um nome de usuário e a sua senha 
# e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Digite seu nome: ")
senha = nome

while senha == nome:
    senha=input("Digite uma senha diferente do nome de usuário: ")
    if senha == nome:
        print("Senha inválida! Tente novamente")
print("Usuário criado!")
