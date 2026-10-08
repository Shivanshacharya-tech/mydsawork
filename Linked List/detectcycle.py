#detect the cycle in the given linked list

def detect_cycle(head):
    slow= head
    fast= head

    while fast and fast.next:
        slow= slow.next
        fast= fast.next.next

        if slow == fast:
            return True

    return False

if __name__ == "__main__":
    class Node:
        def __init__(self, data):
            self.data= data
            self.next= None

    # Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle)
    head= Node(1)
    head.next= Node(2)
    head.next.next= Node(3)
    head.next.next.next= Node(4)
    head.next.next.next.next= Node(5)
    head.next.next.next.next.next= head.next.next  # Creating a cycle

    if detect_cycle(head):
        print("Cycle detected in the linked list.")
    else:
        print("No cycle detected in the linked list.")
        