class Pilha(object):
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []

    def topo(self):
        return self.items[len(self.items) - 1]

    def tamanho(self):
        return len(self.items)

    def empilha(self, element):
        self.items.append(element)

    def desempilha(self):
        return self.items.pop()

    def __str__(self):
        return '{0}'.format(self.items)

class Fila:
    def __init__(self):
        self.fila = []

    def inserir(self, elemento):
        self.fila.append(elemento)

    def excluir(self):
        del self.fila[0]

    def tamanho(self):
        return len(self.fila)

    def iniciodafila(self):
        return self.fila[0]

    def vazia(self):
        return self.tamanho() == 0

    def __str__(self):
        return '{0}'.format(self.fila)




