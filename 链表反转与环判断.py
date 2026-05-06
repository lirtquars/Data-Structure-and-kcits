class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next  
        curr.next = prev      
        prev = curr            
        curr = next_node       
    return prev  
def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

