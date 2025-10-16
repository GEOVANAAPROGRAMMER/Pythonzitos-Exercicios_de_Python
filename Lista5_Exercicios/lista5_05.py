meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

dia, mes, ano = input("Digite uma data no formato dd/mm/aaaa: ").split("/")
data = f"{dia}/{mes}/{ano}"

# Mostrando a data no formato solicitado
print("Data:", dia, "de", meses[int(mes) - 1], "de", ano)