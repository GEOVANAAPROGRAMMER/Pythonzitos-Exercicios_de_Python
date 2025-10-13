n = 1
soma = 0
while n <= 10:
    x = int(input(f"Digite o {n}º número: "))
    soma += x
    n += 1
media = soma / 10
print(f"A soma dos 10 números é: {soma}")
print(f"A média dos 10 números é: {media:.2f}")