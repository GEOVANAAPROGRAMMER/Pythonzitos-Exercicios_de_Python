peso = float(input("Digite o peso (kg) da carga de peixes: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"O peso excede o limite em {excesso:.2f} kg. A multa a ser paga é de R$ {multa:.2f}.")