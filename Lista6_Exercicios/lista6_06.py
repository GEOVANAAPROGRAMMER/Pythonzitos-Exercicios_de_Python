import random

l1 = random.sample(range(100), 10)
l2 = random.sample(range(100), 10)
l3 = []

for i in range(len(l1)):
    l3.append(l1[i])
    l3.append(l2[i])

print(f"Lista 1: {l1}")
print(f"Lista 2: {l2}") 
print(f"Lista 3: {l3}")

print("----------------------------------------")

# Outra forma de fazer o mesmo exercício
l4 = random.sample(range(100), 10)
l5 = random.sample(range(100), 10)
l6 = []

for x in zip(l4, l5):
    l6.extend(list(x))

print(f"Lista 4: {l4}")
print(f"Lista 5: {l5}")
print(f"Lista 6: {l6}")