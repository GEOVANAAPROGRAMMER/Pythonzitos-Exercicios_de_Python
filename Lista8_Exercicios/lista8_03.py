class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2

tv_quarto = Televisão()
tv_sala = Televisão()

print(tv_quarto.ligada)
print(tv_quarto.canal)

tv_sala.ligada = True
print(tv_sala.ligada)

tv_sala.canal = 11
print(tv_sala.canal)