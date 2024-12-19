class Elevador:
    def __init__(self,total_pisos: int):
        self.piso_atual = 0
        self.total_pisos = total_pisos
        

    def subir(self,qtd_andares: int):
        andar_final = self.piso_atual + qtd_andares

        if andar_final > self.total_pisos:
            print('Não é possível subir')
            
        else:
            self.piso_atual = andar_final

        

    def descer(self):
        ...

    def ir_para_piso(self):
        ...

    def exibir_piso_atual(self):
        ...


elevador1 = Elevador(10)

elevador1.subir(3)