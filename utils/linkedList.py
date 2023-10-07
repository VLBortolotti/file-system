class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None

class ListaEnc:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def vazia(self):
        return self.inicio == None
    
    def imprime(self):
        aux = self.inicio
        
        while (aux != None):
            print(f"Valor: {aux.info}")
            aux = aux.prox
    
    def exclui(self, posicao):
        if (not self.vazia() and posicao > 0):
            if (posicao == 1):
                self.inicio = self.inicio.prox
                self.tamanho -= 1

            else:
                i = 1
                aux = self.inicio
                ant = None
                while(i < posicao and aux != None):
                    ant = aux
                    aux = aux.prox
                    i += 1
                
                if (aux != None):
                    ant.prox = aux.prox
                    self.tamanho -= 1
    
    def insere(self, posicao, valor):
        if (posicao > 0):
            novo = Nodo(valor)
            
            if (posicao == 1):
                novo.prox = self.inicio
                self.inicio = novo
                self.tamanho += 1
            
            else:
                aux = self.inicio
                i = 1
                
                while (i < posicao - 1 and aux != None):
                    aux = aux.prox
                    i += 1
                
                if (aux != None):
                    novo.prox = aux.prox
                    aux.prox = novo
                    self.tamanho += 1

    def posicao(self, valor):
        aux = self.inicio
        i = 1
        while (aux != None):
            if (aux.info == valor):
                return i
            aux = aux.prox
            i += 1
        return 0
    
    def valor(self, posicao):
        if (posicao > 0):
            aux = self.inicio
            i = 1
            while (i < posicao and aux != None):
                aux = aux.prox
                i += 1

            if (i == posicao and aux != None):
                return aux.info

        return -1

    def getTamanho(self):
        return self.tamanho
    
    def getTamanhoDois(self):
        aux = self.inicio
        tam = 0

        while (aux != None):
            tam += 1
            aux = aux.prox
        
        return tam
        
    def comparaListas(self, lista2):
        aux1 = self.inicio
        aux2 = lista2.inicio

        if (self.getTamanho() == lista2.getTamanho()):

            while (aux1 != None and aux2 != None):
                if (aux1.info != aux2.info):
                    return False

                aux1 = aux1.prox
                aux2 = aux2.prox

            return True
            
        return False

    def inverterLista(self):
        aux = self.inicio
        listaContigua = []

        while (aux != None):
            listaContigua.append(aux.info)
            aux = aux.prox

        novaLista = ListaEnc()
        
        cont = 1
        for i in range(len(listaContigua)-1, -1, -1):
            novaLista.insere(cont, listaContigua[i])
            cont += 1

        return novaLista
        
    def destroi(self):
        self.inicio = None


lista = ListaEnc()
lista.insere(1, '1')

lista.insere(2, '2')

lista2 = ListaEnc()
lista2.insere(1, '1')
lista2.insere(2, '2')

print("lista")
lista2.imprime()

print("lista invertida")
listaInvertida = lista2.inverterLista()
listaInvertida.imprime()