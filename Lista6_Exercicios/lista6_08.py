texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''.lower()
import string

for i in string.punctuation:
    texto = texto.replace(i, '')
resp = []

cont = 0
for p in texto.split():
    if p[0].lower() in "python" and p[-1].lower() in "python" and len(p) > 4:
        cont += 1
        resp.append(p)

print(resp)
print(cont)