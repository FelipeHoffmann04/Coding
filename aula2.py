class Comodo:
    def __init__(self, nome="", dimensoes=""):
        self.nome = nome
        self.dimensoes = dimensoes

    def __str__(self):
        local = f'{self.nome} de {self.dimensoes}'
        return local

class Mobilia:
    def __init__(self, nome="", funcao="", material="", comodo=None):
        self.nome = nome
        self.funcao = funcao
        self.material = material
        self.comodo = comodo

    def __str__(self): # expressao do objeto em forma textual
        s = f'Mobília: {self.nome}, '+\
               f'funcao:{self.funcao}, feito de {self.material}'

        if self.comodo:
            s += f', localizada em: {str(self.comodo)}'
        return s

class Casa:
    def __init__(self,proprietario = "", formato="", comodos = None):
        self.proprietario = proprietario
        self.formato = formato
        self.comodos = comodos

        if comodos is None: # regra da composicao
            raise Exception("Uma casa precisa ter pelo menos um comodo")
        

    def __str__(self):
        s = f'Casa de {self.proprietario} possui:'

        for comodo in self.comodos:
            s += f'{str(comodo)};'
        return s

if __name__ == "__main__": # teste das classes
    
    c1 = Comodo(nome ="Sala de estar", dimensoes="6mx5m")
    print(c1)
    print()

    c2 = Comodo(nome ="Banheiro", dimensoes="3mx4m")
    c3 = Comodo(nome ="Quarto", dimensoes ="5mx5m")

    m1 = Mobilia(nome = "Sofa", funcao = "Sentar", 
        material = "Couro", comodo = c1) # comodo e opcional
    print(m1)
    print()
    
    m2 = Mobilia(nome = "Cama", funcao = "Repousar",
        material = "Madeira", comodo = c3)
    m3 = Mobilia(nome = "Vaso sanitario", funcao = "Descarregar",
        material = "Porcelana", comodo = c2)

    k1 = Casa(proprietario = "Felipe Jardim Hoffmann", formato="Germanica", comodos=[c1,c2,c3])
    print(k1)