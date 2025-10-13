notas = []
k = 0
soma = 0
while k <= 3:
    notas.append(float(input(f"Digite a nota: ")))
    soma += notas[k]
    k += 1

print(f"A soma das notas é: {soma}")
print(f"A média das notas é: {soma / 4:.2f}")