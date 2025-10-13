a = 80000
b = 200000
i = 0
while a <= b:
    a += a * 0.03
    b += b * 0.015
    i += 1
print(f"Após {i} anos, a população de A será {a:.2f} e a população de B será {b:.2f}.")