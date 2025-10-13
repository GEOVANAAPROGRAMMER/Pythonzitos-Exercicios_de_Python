nota = float(input("Digite a nota do aluno: "))
while nota < 0 or nota > 10:
    print("Nota inválida. Digite uma nota entre 0 e 10.")
    nota = float(input("Digite a nota do aluno: "))
print(f"A nota válida é: {nota}")