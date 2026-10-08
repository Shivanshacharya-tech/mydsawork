#remove n-th node from end of the linked list

# Python3 program to delete nth node from last
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Given the head of a list, remove the Nth node from the end
def remove_nth_from_end(head, N):
  
    # Calculate the length of the linked list
    length = 0
    curr = head
    while curr is not None:
        length += 1
        curr = curr.next

    # Calculate the position to remove from the front
    target = length - N + 1

    # If target is 1, remove the head node
    if target == 1:
        return head.next

    # Traverse to the node just before the target node
    curr = head
    for _ in range(target - 2):
        curr = curr.next

    # Remove the target node
    curr.next = curr.next.next

    return head

def print_list(node):
    curr = node;
    while curr is not None:
        print(f" {curr.data}", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
  
    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    N = 2  
    head = remove_nth_from_end(head, N)

    print_list(head)