def ip_ok (ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True


with open(r'C:\Users\Desktop\Documents\IDE PYTHON\Lista7_Exercicios\IPS.txt', 'r', encoding='utf-8') as arquivo, \
     open(r'C:\Users\Desktop\Documents\IDE PYTHON\Lista7_Exercicios\ip_valido.txt', 'w', encoding='utf-8') as validos, \
     open(r'C:\Users\Desktop\Documents\IDE PYTHON\Lista7_Exercicios\ip_invalido.txt', 'w', encoding='utf-8') as invalidos:
    for linha in arquivo.readlines():
        if ip_ok (linha):
            validos.write(linha)
        else:
            invalidos.write(linha) 
