s = "um tigre, dois tigres, três tigres"
print(s.find("tigre"))  # Retorna 3
print(s.find("tigre", 4))   # Retorna 15
print(s.find("tigre", 16))  # Retorna 28

print(s.replace("tigre", "gato"))  # Substitui todas as ocorrências
