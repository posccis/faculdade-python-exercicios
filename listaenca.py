from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                if pointer.next == self.head:
                    break
                pointer = pointer.next
                
            pointer.next = Node(elem)
            pointer.next.next = self.head
        else: 
            self.head = Node(elem)
        self._size += 1
    
    def __len__(self):

        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        return pointer

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data 
        raise IndexError("List index out of range")
    
    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List index out of range")
    
    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return pointer.next
            pointer = pointer.next
            i += 1

    def insert(self, index, elem):
        if index == 0:
            node = Node(elem)
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node = Node(elem)
            node.next = pointer.next
            pointer.next = node
        self._size += 1
    def remove(self, elem):
        if self.head == None:
            raise IndexError("List index out of range")
        elif self.head.data == elem:
            self.head = self.head.next
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            

            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
        self._size -= 1
                    
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            if pointer.next == self.head:
                break
            
            pointer=pointer.next
        return r
    def som(self):
        soma = 0
        soma_aux = 0
        pointer = self.head
        while (pointer):
            soma_aux += pointer.data
            if soma_aux < 0:
                soma_aux = 0
            elif soma_aux > soma:
                soma = soma_aux
            else:
                soma = soma
            if pointer.next == self.head:
                soma_aux += pointer.next.data
                if soma_aux < 0:
                    soma_aux = 0
                elif soma_aux > soma:
                    soma = soma_aux
                else:
                    soma = soma
                break
            pointer = pointer.next
        return soma

