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

def isPalindrome(list1:LinkedList):
    numbers=[]
    current = list1.head
    while current:
        numbers.append(current.val)
        if current.next:
            current = current.next
        else:
            break
    head_index = 0
    tail_index = -1
    while len(numbers)//2 >= head_index+1:
            if numbers[head_index] == numbers[tail_index]:
                head_index += 1
                tail_index -= 1
            else:
                return False
    return True
    
list1 = LinkedList()
list1.append(4)
list1.append(3)
list1.append(1)
list1.append(3)
list1.append(4)
print(isPalindrome(list1))