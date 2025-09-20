class Fila:
    def __init__(self):
        self.items = []

    def inserir(self, processo):
        self.items.append(processo)

    def remover(self):
        return self.items.pop(0)

    def vazia(self):
        return self.items == []