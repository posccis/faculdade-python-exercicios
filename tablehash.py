class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
class HashTable:
    
    def __init__(self):
        listaEnca = LinkedList()
        self.Max = 10000
        for x in range(self.Max):
            listaEnca.append(None)
        self.arr = listaEnca
    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100
    
    def add(self,key,val):
        h = self.getHash(key)
        self.arr[h] = val


    def __setitem__(self, key, val):
        h = self.getHash(key)
        self.arr[h] = val
    def __getitem__(self, key):
        h = self.getHash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.getHash(key)
        self.arr[h] = None




