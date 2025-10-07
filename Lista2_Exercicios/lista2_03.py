i = 10
while i >= 0:
    print(i)
    i -= 1


print("--------------------------------")

senha_correta = "python123"
senha = input("Digite a senha: ")
while senha != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")
print("Senha correta. Acesso concedido.")