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

def middlenode(list1:LinkedList):
    fast = list1.head
    slow = list1.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    list1.head = slow

    return list1.display()


list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(2)
list1.append(4)
list1.append(0)
list1.append(5)
list1.append(7)
list1.append(6)
middlenode(list1)

