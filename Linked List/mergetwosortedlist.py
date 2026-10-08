#merging two sorted linked lists

def merge_sorted_linkedlists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.data < head2.data:
        head1.next= merge_sorted_linkedlists(head1.next, head2)
        return head1
    else:
        head2.next= merge_sorted_linkedlists(head1, head2.next)
        return head2


if __name__ == "__main__":
    class Node:
        def __init__(self, data):
            self.data= data
            self.next= None

    # Create first sorted linked list: 1 -> 3 -> 5
    head1= Node(1)
    head1.next= Node(3)
    head1.next.next= Node(5)

    # Create second sorted linked list: 2 -> 4 -> 6
    head2= Node(2)
    head2.next= Node(4)
    head2.next.next= Node(6)

    merged_head= merge_sorted_linkedlists(head1, head2)

    # Print the merged linked list
    current= merged_head
    while current:
        print(current.data, end=" ")
        current= current.next