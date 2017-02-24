class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_list(head):
    if not head:
        raise ValueError('Empty head')
    tmp_head = head
    while tmp_head.next:
        print(tmp_head.data, end=' -> ')
        tmp_head = tmp_head.next
    print(tmp_head.data)


def delete(head, key):
    if not head:
        return
    if head.data == key:
        return head.next

    tmp_head = head
    while tmp_head.next:
        if tmp_head.next.data == key:
            tmp_head.next = tmp_head.next.next
            break
        tmp_head = tmp_head.next

    return head


def delete_position(head, position):
    if not head:
        return
    if position == 0:
        return head.next

    i = 0
    tmp_head = head
    prev = None
    while tmp_head and i < position:
        prev = tmp_head
        tmp_head = tmp_head.next
        i += 1

    if tmp_head:
        prev.next = tmp_head.next
    return head


def swap_nodes(head, x, y):
    if x == y:
        return head
    x_prev = y_prev = x_node = y_node = prev = None

    tmp_head = head
    while tmp_head and not (x_node and y_node):
        if tmp_head.data == x:
            x_node = tmp_head
            x_prev = prev
        if tmp_head.data == y:
            y_node = tmp_head
            y_prev = prev
        prev = tmp_head
        tmp_head = tmp_head.next

    if not (x_node and y_node):
        return head

    if not x_prev:
        head = y_node
    else:
        x_prev.next = y_node

    if not y_prev:
        head = x_node
    else:
        y_prev.next = x_node

    next_y = y_node.next
    y_node.next = x_node.next
    x_node.next = next_y
    return head


def sorted_merge(head1, head2):
    if not head1:
        return head2
    elif not head2:
        return head1
    tmp_head1 = head1
    tmp_head2 = head2

    new_head = Node(None)
    new_head_copy = new_head

    while tmp_head1 and tmp_head2:
        if tmp_head1.data < tmp_head2.data:
            new_head.next = tmp_head1
            tmp_head1 = tmp_head1.next
        else:
            new_head.next = tmp_head2
            tmp_head2 = tmp_head2.next

        new_head = new_head.next

    if tmp_head1:
        new_head.next = tmp_head1
    else:
        new_head.next = tmp_head2

    return new_head_copy.next


def merge_recursive(head1, head2):
    if not head1:
        return head2
    elif not head2:
        return head1
    if head1 == head2:
        return head1

    if head1.data < head2.data:
        new_head = head1
        new_head.next = merge_recursive(head1.next, head2)
    else:
        new_head = head2
        new_head.next = merge_recursive(head2.next, head1)
    return new_head


def mergesort(head):
    if not head:
        return

    head_copy = slow = fast = head
    while fast.next:
        fast = fast.next
        if fast.next:
            fast = fast.next
            slow = slow.next

    if slow == fast:
        return slow

    right_head = slow.next
    slow.next = None
    new_left_head = mergesort(head_copy)
    new_right_head = mergesort(right_head)
    return sorted_merge(new_left_head, new_right_head)


def reverse_in_group(head, size):
    if not head or size < 1:
        raise ValueError('Bad input')

    counter = 0
    new_head = left = head
    prev = None
    right = head
    while right:
        if counter != 0 and counter % size == 0:
            counter = 0
            if not new_head:
                new_head = right
            left.next = right.next

        next_head = right.next
        right.next = prev
        prev = right
        right = next_head
    return new_head

    0 1 2 3 4


n8 = Node(2)
n7 = Node(2, n8)
n6 = Node(3, n7)
n5 = Node(5, n6)
n4 = Node(2, n5)
n3 = Node(1, n4)
n2 = Node(3, n3)
n1 = Node(6, n2)


print_list(n1)
print_list(mergesort(n1))