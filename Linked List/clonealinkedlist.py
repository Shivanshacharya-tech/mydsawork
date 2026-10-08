#clone a linked list with next and random pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

    def clone_linkedlist(head):
        if not head:
            return None

        # Step 1: Create a copy of each node and insert it next to the original node
        current = head
        while current:
            new_node = Node(current.data)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Set the random pointers for the copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the original and copied linked lists
        original_current = head
        copy_current = head.next
        copy_head = head.next

        while original_current:
            original_current.next = original_current.next.next
            if copy_current.next:
                copy_current.next = copy_current.next.next
            original_current = original_current.next
            copy_current = copy_current.next

        return copy_head


if __name__ == "__main__":
    # Create a linked list with random pointers
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    # Set random pointers
    head.random = head.next.next  # 1's random points to 3
    head.next.random = head        # 2's random points to 1
    head.next.next.random = head.next.next.next  # 3's random points to 4
    head.next.next.next.random = head.next       # 4's random points to 2

    # Clone the linked list
    cloned_head = Node.clone_linkedlist(head)

    # Print the original and cloned linked lists with their random pointers
    def print_linkedlist_with_random(head):
        current = head
        while current:
            random_data = current.random.data if current.random else None
            print(f"Node data: {current.data}, Random points to: {random_data}")
            current = current.next

    print("Original Linked List:")
    print_linkedlist_with_random(head)

    print("\nCloned Linked List:")
    print_linkedlist_with_random(cloned_head)
    