class Televisao:
    # Contrutor: configura a inicialização da classe
    def __init__ (self):
        self.ligado = False
        self.canal = 2
    
    #Métodos
    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1


tv = Televisao()
print(tv.ligado)
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)

tv.muda_canal_para_cima()
tv.muda_canal_para_cima() 
print(tv.canal)