from fila import Fila

class FilaCPU(Fila):
    def __init__(self):
        super().__init__()

    def inserir(self, processo):    
        pos = 0  
        for p in self.items:
            if processo.prioridade < p.prioridade:
                break 
            pos += 1        
        self.items.insert(pos, processo)
