min = float(input("Digite um valor em minutos: "))
if min < 200:
    custo = 0.20 * min
    print(f"O custo da ligação é de R$ {custo:.2f}")
elif 200 <= min < 400:
    custo = 0.18 * min
    print(f"O custo da ligação é de R$ {custo:.2f}")
elif 400 <= min < 800:
    custo = 0.15 * min
    print(f"O custo da ligação é de R$ {custo:.2f}")
else:
    custo = 0.08 * min
    print(f"O custo da ligação é de R$ {custo:.2f}")