# Texto original (três aspas permitem escrever texto longo em várias linhas)
texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''.lower()
# Importa o módulo string (que tem, entre outras coisas, a lista de pontuações)
import string

# Percorre cada sinal de pontuação (.,!? etc.)
for i in string.punctuation:
    # Substitui cada sinal de pontuação por nada (remove)
    texto = texto.replace(i, '')

# Cria uma lista vazia para armazenar as palavras que atendem à condição
resp = []

# Percorre cada palavra separada no texto
for p in texto.split():  # .split() separa o texto nos espaços em branco
    # Verifica se a primeira letra (p[0]) ou a última (p[-1]) da palavra
    # está contida na string "python" (ou seja, se é p, y, t, h, o ou n)
    if p[0].lower() in "python" or p[-1].lower() in "python":
        # Se a condição for verdadeira, adiciona a palavra à lista 'resp'
        resp.append(p)

# Exibe a lista de palavras que atendem ao critério
print(resp)
