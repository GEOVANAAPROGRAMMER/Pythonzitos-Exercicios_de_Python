soma = 0
i = 0
while True:
    x = int(input("Digite um número inteiro positivo (ou um 0 para sair): "))
    if x == 0:
        break
    else:
        i += 1
    soma += x
print(f"A soma dos números digitados é: {soma}")
print(f"A média dos números digitados é: {soma / i}")
    