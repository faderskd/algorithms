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

# O(n)
def find_and_remove_loop(head):
    nodes = set()
    prev = None
    head_copy = head
    while head:
        if head in nodes:
            prev.next = None
            break
        nodes.add(head)
        prev = head
        head = head.next
    return head_copy


# O(n^2)
def detect_and_remove_loop(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.net
        slow = slow.next
        if fast == slow:
            remove_loop(head, slow)
    return head

# O(n^2)
def remove_loop(head, loop_node):
    left = head
    while True:
        right = loop_node
        while left != right.next and right.next != loop_node:
            right = right.next
        if left == right.next:
            right.next = None
            return
        left = left.next

# O(n^2)
def rotate_right(head, size):
    if not (head and head.next):
        return head

    first = head
    prev = None
    for i in range(size):
        while head.next:
            prev = head
            head = head.next
        head.next = first
        prev.next = None
        first = head
    return head


def rotate_left(head, size):
    if size < 1:
        return head

    counter = 1
    tmp_head = head
    while counter < size and tmp_head:
        tmp_head = tmp_head.next
        counter += 1

    if not (tmp_head and tmp_head.next):
        return head

    new_head = tmp_head.next
    tmp_head.next = None
    tmp_head = new_head
    while tmp_head.next:
        tmp_head = tmp_head.next
    tmp_head.next = head
    return new_head


n8 = Node(8)
n7 = Node(7, n8)
n6 = Node(6, n7)
n5 = Node(5, n6)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n8.next = n1

print_list(find_and_remove_loop(n1))