import random

print(random.randint(1, 100))

# Escolher um nome aleatório
nomes = "zé lia pedro luiz".split()
print(random.choice(nomes))

# Embaralhar uma lista
random.shuffle(nomes)
print(nomes)

# Escolher 10 números diferentes entre 0 e 99
print(random.sample(range(100), 10))