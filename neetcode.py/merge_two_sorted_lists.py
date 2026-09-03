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

def mergeTwoLists( list1, list2) :
        current1 = list1.head
        current2 = list2.head
        if current1.name >= current2.name:
            while current2.next is not None:
                if current1== current2 or current1.next.name >= current2.name:
                    if current1.next is None:
                        current1.next = current2
                    first_list = current1.next
                    second_list = current2.next
                    current2.next = None
                    current1.next = current2
                    current2.next = first_list
                    current = first_list
                    while current.next is not None:
                        current = current.next
                    current.next = second_list
                
                    return list1.display()
                    
                    
                    
                
        
                        
                            

lista1= LinkedList()
lista1.append(6)
lista1.append(1)
lista1.append(3)
lista1.append(4)
#lista1.display()
lista2 = LinkedList()
lista2.append(2)
lista2.append(2)
lista2.append(4)
#print(lista2.head.name)
(mergeTwoLists(lista1,lista2))

    