import random

lista = random.sample(range(100), 10)
print(lista)
maior = lista[0]
menor = lista[0]

for i in lista:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

print(f"Maior: {maior}")
print(f"Menor: {menor}")