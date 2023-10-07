class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def empty(self):
        return self.inicio == None
    
    def printList(self):
        aux = self.inicio
        
        while (aux != None):
            print(f"value: {aux.info}")
            aux = aux.next
    
    def deleteNode(self, position):
        if (not self.empty() and position > 0):
            if (position == 1):
                self.inicio = self.inicio.next
                self.tamanho -= 1

            else:
                i = 1
                aux = self.inicio
                ant = None
                while(i < position and aux != None):
                    ant = aux
                    aux = aux.next
                    i += 1
                
                if (aux != None):
                    ant.next = aux.next
                    self.tamanho -= 1
    
    def insert(self, position, value):
        if (position > 0):
            novo = Node(value)
            
            if (position == 1):
                novo.next = self.inicio
                self.inicio = novo
                self.tamanho += 1
            
            else:
                aux = self.inicio
                i = 1
                
                while (i < position - 1 and aux != None):
                    aux = aux.next
                    i += 1
                
                if (aux != None):
                    novo.next = aux.next
                    aux.next = novo
                    self.tamanho += 1

    def position(self, value):
        aux = self.inicio
        i = 1
        while (aux != None):
            if (aux.info == value):
                return i
            aux = aux.next
            i += 1
        return 0
    
    def value(self, position):
        if (position > 0):
            aux = self.inicio
            i = 1
            while (i < position and aux != None):
                aux = aux.next
                i += 1

            if (i == position and aux != None):
                return aux.info

        return -1

    def getSize(self):
        return self.tamanho
        
    def compareLists(self, lista2):
        aux1 = self.inicio
        aux2 = lista2.inicio

        if (self.getSize() == lista2.getSize()):

            while (aux1 != None and aux2 != None):
                if (aux1.info != aux2.info):
                    return False

                aux1 = aux1.next
                aux2 = aux2.next

            return True
            
        return False

    def reverseList(self):
        aux = self.inicio
        listaContigua = []

        while (aux != None):
            listaContigua.append(aux.info)
            aux = aux.next

        novaLista = LinkedList()
        
        cont = 1
        for i in range(len(listaContigua)-1, -1, -1):
            novaLista.insert(cont, listaContigua[i])
            cont += 1

        return novaLista
        
    def destroy(self):
        self.inicio = None


lista = LinkedList()
lista.insert(1, '1')

lista.insert(2, '2')

lista2 = LinkedList()
lista2.insert(1, '1')
lista2.insert(2, '2')

print("lista")
lista2.printList()

print("lista invertida")
listaInvertida = lista2.reverseList()
listaInvertida.printList()

print(lista.getSize())
print(lista.position(2))