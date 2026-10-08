#reverse a linked list 

def reverse_linkedlist(head):
    prev= None
    current= head
    while current:
        next_node= current.next
        current.next= prev
        prev= current
        current= next_node
    return prev

def print_linkedlist(head):
    current= head
    while current:
        print(current.data, end=" ")
        current= current.next
    print()


if __name__ == "__main__":
    class Node:
        def __init__(self, data):
            self.data= data
            self.next= None

    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head= Node(1)
    head.next= Node(2)
    head.next.next= Node(3)
    head.next.next.next= Node(4)
    head.next.next.next.next= Node(5)

    print("Original Linked List:")
    print_linkedlist(head)

    reversed_head= reverse_linkedlist(head)

    print("Reversed Linked List:")
    print_linkedlist(reversed_head)