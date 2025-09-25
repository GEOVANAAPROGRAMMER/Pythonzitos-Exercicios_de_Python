stop = ""

while stop != "s":
    # População A
    A = int(input("Digite a população do país A (maior que 0): "))
    while A <= 0:
        print("A população deve ser maior que 0.")
        A = int(input("Digite a população do país A (maior que 0): "))

    taxaA = float(input("Digite a taxa de crescimento do país A (em %): ")) / 100

    # População B
    B = int(input("Digite a população do país B (maior que 0): "))
    while B <= 0:
        print("A população deve ser maior que 0.")
        B = int(input("Digite a população do país B (maior que 0): "))

    taxaB = float(input("Digite a taxa de crescimento do país B (em %): ")) / 100

    anos = 0

    # Cálculo
    while A < B:
        A += A * taxaA
        B += B * taxaB
        anos += 1

    print(f"\n✅ Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.\n")
    stop = input("Deseja sair? (s/n): ").lower()

print("Programa finalizado!")
