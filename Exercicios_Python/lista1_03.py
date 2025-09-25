# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = ""
idade = -1
salario = -1.0
sexo = ""
estCivil = ""

while len(nome) < 3:
    print("O nome deve ter mais que 3 caracteres. ")
    nome = input("Digite seu nome: ")

print("Nome adicionado! ")

while idade < 0 or idade > 150:
    print("A idade deve estar entre 0 e 150 anos. ")
    idade = int(input("Digite sua idade: "))
print("Idade adicionada! ")

while salario <= 0:
    print("O salário deve ser maior que zero. ")
    salario = float(input("Digite seu salário: "))
print("Salário adicionado! ")

while sexo not in ['f', 'm']:
    print("O sexo deve ser 'f' ou 'm'. ")
    sexo = input("Digite seu sexo (f/m): ").lower()
print("Sexo adicionado! ")

while estCivil not in ['s', 'c', 'v', 'd']:
    print("O estado civil deve ser 's', 'c', 'v' ou 'd'. ")
    estCivil = input("Digite seu estado civil (s/c/v/d): ").lower()
print("Estado civil adicionado! ")
