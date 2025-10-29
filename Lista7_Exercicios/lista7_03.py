# Gravando linhas em um arquivo de texto
f = open(r'C:\Users\Desktop\Documents\IDE PYTHON\Lista7_Exercicios\arquivo.txt', 'w')

for linha in range(1, 101):
    f.write(f'Esta é a linha {linha}\n')
f.close()

# Lendo o arquivo
f = open(r'C:\Users\Desktop\Documents\IDE PYTHON\Lista7_Exercicios\arquivo.txt', 'r')

# Lê todas as linhas e imprime uma a uma, removendo espaços e quebras de linha
for linha in f.readlines():
    print(linha.strip())
f.close()

print("_________________________________________________________________________")

# Lendo o arquivo usando 'with'
with open(r'C:\Users\Desktop\Documents\IDE PYTHON\Lista7_Exercicios\arquivo.txt', 'r') as f:
    print(f.read())