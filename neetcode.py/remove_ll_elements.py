class ListNode:
    def __init__(self,val: int):
        self.val = val
        self.next = None
        pass

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 
        pass

    def append(self,val:str):
        self.size += 1
        new_person = ListNode(val)
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
            x.append(str(current.val))
           
            current = current.next
        print(" -> ".join(x))


def removeElements( list1: ListNode,val:int):
    if list1.head is None:
        return None
    current = list1.head
    #first lets set the right head
    while current is not None and current.val == val:
           
           if current.next:
             list1.head = current.next
             current = current.next
           else:
             return None 


    while current.next:
        if current.next.val == val:
            if current.next.next:
                current.next = current.next.next
            else:
                current.next = None
                break
        else:
            current = current.next
        
    return list1.display()


list1= LinkedList()
list1.append(1)
list1.append(2)
list1.append(6)
list1.append(3)
list1.append(4)
list1.append(5)
list1.append(6)
list1.append(2)
removeElements(list1,6)
#Wprint(removeElements(list1,2))




