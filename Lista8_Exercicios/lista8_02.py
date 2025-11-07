import string

texto = open('Lista8_Exercicios/cachorro.txt', 'r', encoding='utf-8').read().lower()
for i in string.punctuation:
    texto = texto.replace(i, '')

palavras = texto.split()

wc = {}

for p in palavras:
    # Verifica se a palavra já está no dicionário, caso esteja, 
    # incrementa o contador e adiciona a palavra e o valor no dicionário
    if p in wc:
        wc[p] += 1 
        
    else:
        wc[p] = 1

def ordenar_por_frequencia(itens):
    return itens[1]

duplas_ordenadas = sorted(wc.items(), key=ordenar_por_frequencia, reverse=True)

for k in duplas_ordenadas[:10]:
    print(k[0], k[1])