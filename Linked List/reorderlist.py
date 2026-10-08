#reorder the linked list in the following way: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …


def reorder_linkedlist(head):
    if not head or not head.next:
        return head

    # Step 1: Find the middle of the linked list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Step 3: Merge the two halves
    first_half = head
    second_half = prev

    while second_half.next:
        temp1 = first_half.next
        temp2 = second_half.next

        first_half.next = second_half
        second_half.next = temp1

        first_half = temp1
        second_half = temp2

    return head

if __name__ == "__main__":
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original Linked List:")
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

    reordered_head = reorder_linkedlist(head)

    print("Reordered Linked List:")
    current = reordered_head
    while current:
        print(current.data, end=" ")
        current = current.next
        