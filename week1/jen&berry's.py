class Node:
    def __init__(self, name: str):
        self.name = name
        self.next = None
        pass
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 
        pass
    def append(self,name:str):
        self.size += 1
        new_person = Node(name)
        if self.head is None:
            self.head = new_person
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_person

    def display(self):
        current = self.head
        x  = []
        while current is not None:
            x.append(str(current.name))
           
            current = current.next
        print(" -> ".join(x))
    
def reorder_students(L):
    n = 0
    current = L.head
    while current is not None:
        n += 1
        if n == L.size/2:
            second_half = current.next
            current.next = None
            curr = second_half
            prev = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            current.next = prev
            return
        current = current.next

    
lista = LinkedList()
lista.append("Asia")
lista.append("Basia")
lista.append("Celina")
lista.append("Daria")
lista.append("Emilia")
lista.append("Frania")
#print(lista.size)
lista.display()
reorder_students(lista)
lista.display()
