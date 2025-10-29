def fatorial(n):
    fatorial = 1
    for i in range(n, 0, -1):
        fatorial *= i
    return fatorial


print(fatorial(5))