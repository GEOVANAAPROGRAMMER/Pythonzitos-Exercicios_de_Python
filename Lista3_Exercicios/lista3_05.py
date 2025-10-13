n = (int(input("Digite um número inteiro positivo: ")))
fat = 1
while n > 1:
    fat *= n
    n -= 1  
print(f"O fatorial é: {fat}")