import random

lista = random.sample(range(100), 20)
par = []
impar = []

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f"Lista completa: {lista}")
print(f"Lista de números pares: {par}")
print(f"Lista de números ímpares: {impar}")