import this

# a = 42 + "abacate"
# print(a)

a = (str(42) + " abacate")
print(a)

print(a.upper())
print(a.lower())

# Troca uma substring por outra
print(a.replace("abacate", "laranja"))

# Verifica se uma substring está contida na string
print("abacate" in a)

# Verifica se uma substring não está contida na string
print("abacate" not in a)

# Divide a string em uma lista de substrings
print(a.split(" "))

# Verifica se a string começa com uma substring
print(a.startswith("42"))

# Verifica se a string termina com uma substring
print(a.endswith("laranja"))

a = 3
b = "abacate"
a,b = b, a
print(a, b)

# Formatação de data
d, m, a = 25, 12, 2024
print(f"{d:02}/{m:02}/{a}")
