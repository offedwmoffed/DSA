class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

# Funkcje pomocnicze do testowania
def build_linked_list(elements):
    dummy = ListNode()
    curr = dummy
    for val in elements:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) if vals else "Pusta lista")

# Test działania
if __name__ == "__main__":
    # Przygotowanie list wejściowych: [1, 2, 4] oraz [1, 3, 4]
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])

    sol = Solution()
    merged = sol.mergeTwoLists(list1, list2)

    # Wynik: 1 -> 1 -> 2 -> 3 -> 4 -> 4
    print_linked_list(merged)