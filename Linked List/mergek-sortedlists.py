#merging k sorted linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_two_lists(l1, l2):
    """Helper function to merge two sorted linked lists."""
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next


def merge_k_sorted_linkedlists(lists):
    """Divide and conquer approach to merge k sorted linked lists."""
    if not lists:
        return None

    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            # Use helper function to merge two individual lists
            merged_lists.append(merge_two_lists(l1, l2))
        lists = merged_lists

    return lists[0]


if __name__ == "__main__":
    # Create 3 sorted linked lists
    list1 = Node(1)
    list1.next = Node(4)
    list1.next.next = Node(7)

    list2 = Node(2)
    list2.next = Node(5)
    list2.next.next = Node(8)

    list3 = Node(3)
    list3.next = Node(6)
    list3.next.next = Node(9)

    lists = [list1, list2, list3]

    merged_head = merge_k_sorted_linkedlists(lists)

    # Print the merged linked list
    current = merged_head
    while current:
        print(current.data, end=" ")
        current = current.next