from unidecode import unidecode

with open(r'C:\Users\Desktop\Documents\IDE PYTHON\Lista7_Exercicios\batatinha.txt', 'r', encoding='utf-8') as texto, \
     open(r'C:\Users\Desktop\Documents\IDE PYTHON\Lista7_Exercicios\batatinha__cripto.txt', 'w', encoding='utf-8') as cripto:

    for linhaInteira in texto:
        for caracter in linhaInteira:
            caracter = unidecode(caracter).lower()  # Remove acentuação e converte para minúsculas
            if caracter in 'aeiou':
                cripto.write('*')
            else:
                cripto.write(caracter)

print("Arquivo criptografado com sucesso!")

# Se quiser ver o conteúdo criptografado:
with open(r'C:\Users\Desktop\Documents\IDE PYTHON\Lista7_Exercicios\batatinha__cripto.txt', 'r', encoding='utf-8') as resultado:
    print(resultado.read())
