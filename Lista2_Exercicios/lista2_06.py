velocidade = int(input("Digite a velocidade do carro em km/h: "))
if velocidade > 110:
    print("Você foi multado!")
    multa = (velocidade - 110) * 5
    print(f"O valor da multa é de R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade.")