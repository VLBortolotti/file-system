from linkedList import * # classe com lista simplesmente encadeada

class FAT:
    # inicializa File Allocation Table com o numero de entradas (blocos) desejada
    def __init__(self, num_entries):
        self.entries = LinkedList()

        for _ in range(num_entries):
            self.entries.insert(1, -1) # entradas desocupadas

        # Dicionario com informacoes de alocacao dos arquivos
        self.file_allocation = {} # arquivo: [blocos]

    # Encontra e aloca um bloco livre para um arquivo
    def allocate_block(self, file_id):
        if file_id not in self.file_allocation: # significa que eh um arquivo novo
            self.file_allocation[file_id] = []

        for i in range(1, self.entries.getSize() + 1):
            if self.entries.getValueByPosition(i) == -1: # se a entrada estiver livre

                self.entries.insert(i, i)               # marca o bloco como alocado
                self.file_allocation[file_id].append(i) # adiciona o bloco alocado ao arquivo
                return i

        return -1 # nao ha blocos livres

    # Desaloca um bloco para um arquivo, marcando-o como livre (-1)
    def deallocate_block(self, file_id, block_index):
        # se o arquivo existe, e o bloco esta sendo utilizado por este arquivo
        if file_id in self.file_allocation and block_index in self.file_allocation[file_id]:
            self.entries.insert(block_index, -1)                # marcar bloco como livre
            self.file_allocation[file_id].remove(block_index)   # e remove-lo da lista de blocos do arquivo

            return True # bloco desalocado

        return False    # bloco ou arquivo invalidos/nao-existentes
    
    # recebe o id do arquivo, e o numero de blocos (file_size)
    def allocate_file(self, file_id, file_size):
        allocated_blocks = [] # blocos alocados para o arquivo

        # buscar blocos livres para a quantidade de blocos necessarios
        for _ in range(file_size):
            block = self.allocate_block(file_id)  # retorna o indice de um bloco livre para o arquivo  

            if block != -1:                     # se bloco estiver livre
                allocated_blocks.append(block)  # adiciona-lo a lista de blocos

            else: # se a alocacao falhar para algum bloco, desalocar todos os blocos da lista
                for allocated_block in allocated_blocks:
                    self.deallocate_block(file_id, allocated_block)

                return False # arquivo nao alocado
            
        return True # arquivo alocado

    # imprime o FAT
    def print_fat(self):
        self.entries.printList()