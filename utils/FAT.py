from linkedList import * # classe com lista simplesmente encadeada

class FAT:
    # inicializa File Allocation Table com o numero de entradas desejada
    def __init__(self, num_entries):
        self.entries = LinkedList()

        for _ in range(num_entries):
            self.entries.insert(1, -1) # entradas desocupadas

    # Encontra e aloca um bloco livre
    def allocate_block(self):
        for i in range(1, self.entries.getSize() + 1):
            if self.entries.getValueByPosition(i) == -1: # se a entrada estiver livre

                self.entries.insert(i, i) # marca o bloco como alocado
                return i

        return -1 # nao ha blocos livres

    # desaloca um bloco e marca-o como livre (-1)
    def deallocate_block(self, block_index):
        if 1 <= block_index <= self.entries.getSize(): # verifica se um bloco valido
            self.entries.insert(block_index, -1)       # e marca-o
            return True

        return False # indice de bloco nao eh valido

    # imprime o FAT
    def print_fat(self):
        self.entries.printList()
