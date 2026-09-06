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
