palavra = input("Digite uma palavra: ")
i = 0
troca = ""

# in Significa que a letra está dentro da string
while i < len(palavra):
    if palavra[i] in "aeiouAEIOU":
        troca += "*"
    else:
        troca += palavra[i]
    i += 1

# Mostrando a palavra original em maiúsculo e a palavra com as trocas
print(palavra.upper())
print(troca)