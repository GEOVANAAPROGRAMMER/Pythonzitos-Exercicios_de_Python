import random
num = random.randint(1, 100)
tentativa = int(input("Tente adivinhar o número entre 1 e 100: "))

while num != tentativa:
    if tentativa < num:
        print("Tente um número maior.")
    elif tentativa > num:
        print("Tente um número menor.")
    tentativa = int(input("Qual é o seu palpite? "))

print("Parabéns! Você adivinhou o número.")