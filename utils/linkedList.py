class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.size = 0

    def empty(self):
        return self.start == None
    
    def printList(self):
        aux = self.start
        
        while (aux != None):
            print(f"value: {aux.info}")
            aux = aux.next
    
    def deleteNode(self, position):
        if (not self.empty() and position > 0):
            if (position == 1):
                self.start = self.start.next
                self.size -= 1

            else:
                i = 1
                aux = self.start
                ant = None
                while(i < position and aux != None):
                    ant = aux
                    aux = aux.next
                    i += 1
                
                if (aux != None):
                    ant.next = aux.next
                    self.size -= 1
    
    def insert(self, position, value):
        if (position > 0):
            novo = Node(value)
            
            if (position == 1):
                novo.next = self.start
                self.start = novo
                self.size += 1
            
            else:
                aux = self.start
                i = 1
                
                while (i < position - 1 and aux != None):
                    aux = aux.next
                    i += 1
                
                if (aux != None):
                    novo.next = aux.next
                    aux.next = novo
                    self.size += 1

    def getPositionByValue(self, value):
        aux = self.start
        i = 1

        while (aux != None):
            if (aux.info == value):
                return i
            aux = aux.next
            i += 1

        return 0
    
    def getValueByPosition(self, position):
        if (position > 0):
            aux = self.start
            i = 1
            
            while (i < position and aux != None):
                aux = aux.next
                i += 1

            if (i == position and aux != None):
                return aux.info

        return -1

    def getSize(self):
        return self.size
        
    def compareLists(self, list2):
        aux1 = self.start
        aux2 = list2.start

        if (self.getSize() == list2.getSize()):

            while (aux1 != None and aux2 != None):
                if (aux1.info != aux2.info):
                    return False

                aux1 = aux1.next
                aux2 = aux2.next

            return True
            
        return False

    def reverseList(self):
        aux = self.start
        contiguousList = []

        while (aux != None):
            contiguousList.append(aux.info)
            aux = aux.next

        newList = LinkedList()
        
        cont = 1
        for i in range(len(contiguousList)-1, -1, -1):
            newList.insert(cont, contiguousList[i])
            cont += 1

        return newList
        
    def destroyList(self):
        self.start = None

# lista = LinkedList()
# lista.insert(1, '1')

# lista.insert(2, '2')

# list2 = LinkedList()
# list2.insert(1, '1')
# list2.insert(2, '2')

# print("lista")
# list2.printList()

# print("lista invertida")
# listaInvertida = list2.reverseList()
# listaInvertida.printList()

# print(lista.getSize())
# print(lista.getPositionByValue(2))