import sys


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


def insert_to_tree_iterative(root, x):
    if not root:
        return Node(x)

    root_copy = root
    curr = root
    while True:
        if curr.data > x:
            if not curr.left:
                curr.left = Node(x)
                break
            curr = curr.left
        elif curr.data < x:
            if not curr.right:
                curr.right = Node(x)
                break
            curr = curr.right
        else:
            break
    return root_copy


def insert_to_tree_recursive(root, x):
    if not root:
        return Node(x)

    if root.data > x:
        root.left = insert_to_tree_recursive(root.left, x)
    elif root.data < x:
        root.right = insert_to_tree_recursive(root.right, x)
    return root


def search_in_binary_tree(root, x):
    if not root or root.data == x:
        return root
    if x > root.data:
        return search_in_binary_tree(root.right, x)
    return search_in_binary_tree(root.left, x)


def print_tree(root, counter=0):
    if not root:
        return

    print_tree(root.right, counter + 1)
    print('     ')
    print('      ' * counter + str(root.data))
    print_tree(root.left, counter + 1)


def print_given_level(root, level):
    if not root:
        return

    if level == 0:
        print(root.data, end=' ')
        return
    print_given_level(root.left, level - 1)
    print_given_level(root.right, level - 1)


def tree_height(root):
    if not root:
        return 0

    l_height = tree_height(root.left)
    r_height = tree_height(root.right)
    return max(l_height, r_height) + 1


def breath_first_search(root, height):
    for i in range(height):
        print_given_level(root, i)
        print('\n')


def diameter_of_tree(root):
    if not root:
        return 0, 0

    left_height, left_diameter = diameter_of_tree(root.left)
    right_height, right_diameter = diameter_of_tree(root.right)
    height = max(left_height, right_height) + 1

    height_diameter  = left_height + right_height + 1
    return height, max(height_diameter, left_diameter, right_diameter)


def inorder_iterative(root):
    if not root:
        return

    stack = []
    while root or stack:
        if not root:
            root = stack.pop()
            print(root.data, end=' ')
            root = root.right
        else:
            stack.append(root)
            root = root.left


def find_inorder_successor(root):
    if not root:
        return
    if not root.left:
        return root
    return find_inorder_successor(root.left)


def find_inorder_predecessor(root):
    if not root:
        return
    if not root.right:
        return root
    return find_inorder_predecessor(root.right)


def delete_node(root, x):
    if not root:
        return
    if root.data == x:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        successor = find_inorder_successor(root.right)
        root.data = successor.data
        delete_node(root.right, successor.data)
    elif root.data > x:
        root.left = delete_node(root.left, x)
    else:
        root.right = delete_node(root.right, x)
    return root


def job_scheduler_insert(root, x, k):
    if not root:
        return Node(x)

    if (root.data + k > x and root.data < x) or (x + k > root.data and x < root.data):
        raise ValueError('Value %d collides with %d' % (x, root.data))
    if root.data > x:
        root.left = job_scheduler_insert(root.left, x, k)
    elif root.data < x:
        root.right = job_scheduler_insert(root.right, x, k)
    return root


def find_outer_keys_gfg(root, x):
    if not root:
        return
    if root.data == x:
        find_outer_keys_gfg.predecessor = find_inorder_predecessor(root.left)
        find_outer_keys_gfg.successor = find_inorder_successor(root.right)
    if root.data > x:
        find_outer_keys_gfg.successor = root
        find_outer_keys_gfg(root.left, x)
    elif root.data < x:
        find_outer_keys_gfg.predecessor = root
        find_outer_keys_gfg(root.right, x)


def find_max(root):
    if not root:
        return -sys.maxsize
    return max(find_max(root.left), find_max(root.right), root.data)


def find_min(root):
    if not root:
        return sys.maxsize
    return min(find_min(root.left), find_min(root.right), root.data)


# O(n^2)
def check_is_bst_not_efficient(root):
    if not root:
        return True
    if root.data <= find_max(root.left) or root.data >= find_min(root.right):
        return False
    return check_is_bst_not_efficient(root.left) and check_is_bst_not_efficient(root.right)


# O(n)
def check_is_bst(root):
    if not root:
        return
    min_v = max_v = root.data
    if root.left:
        min_l, max_l = check_is_bst(root.left)
        if max_l >= root.data:
            check_is_bst.is_bst = False
        min_v = min_l
    if root.right:
        min_r, max_r = check_is_bst(root.right)
        if min_r <= root.data:
            check_is_bst.is_bst = False
        max_v = max_r
    return min_v, max_v


# O(n)
def check_is_bst_gfg(root, min_v=-sys.maxsize, max_v=sys.maxsize):
    if not root:
        return True
    if root.data >= max_v or root.data <= min_v:
        return False
    return check_is_bst_gfg(root.left, min_v, root.data) and check_is_bst_gfg(root.right, root.data, max_v)


# O(n)
def check_is_bst_by_prev(root):
    if not root:
        return True
    if not check_is_bst_by_prev(root.left):
        return False
    if check_is_bst_by_prev.prev and check_is_bst_by_prev.prev.data >= root.data:
        return False
    check_is_bst_by_prev.prev = root
    return check_is_bst_by_prev(root.right)
check_is_bst_by_prev.prev = None


# O(n) - require firstly search if both elements exists
def find_common_ancestor(root, n1, n2):
    if not root:
        return
    if root.data > n1 and root.data > n2:
        return find_common_ancestor(root.left, n1, n2)
    if root.data < n1 and root.data < n2:
        return find_common_ancestor(root.right, n1, n2)
    return root.data


# O(log(n))
def inorder_successor(root, x):
    node = search_in_binary_tree(root, x)
    if not node:
        return
    if node.right:
        return find_inorder_successor(node.right).data
    successor = None
    while root.data != x:
        if root.data < x:
            root = root.right
        else:
            successor = root
            root = root.left
    return successor.data if successor else None


# O(n)
def k_th_smallest_element(root, k):
    counter = 0

    def k_th_smallest_element_helper(root):
        nonlocal counter
        if not root:
            return
        node = k_th_smallest_element_helper(root.left)
        if node:
            return node
        counter += 1
        if counter == k:
            return root
        return k_th_smallest_element_helper(root.right)

    found = k_th_smallest_element_helper(root)

    return found.data if found else None


def k_th_smallest_element_gfg(root, k):
    if not root:
        return
    counter = 0
    stack = []
    while root:
        stack.append(root)
        root = root.left

    while stack:
        root = stack.pop()
        counter += 1
        if counter == k:
            return root.data
        root = root.right

        while root:
            stack.append(root)
            root = root.left


def merge_two_trees(root1, root2):
    stack1 = []
    stack2 = []

    if not root1:
        inorder_iterative(root2)
        return
    if not root2:
        inorder_iterative(root1)
        return

    root1_changed = True
    root2_changed = True
    while (root1 or stack1) and (root2 or stack2):
        if not root1 or not root2:
            if not root1:
                root1 = stack1.pop()
            if not root2:
                root2 = stack2.pop()

            if root1.data > root2.data:
                print(root2.data, end=' ')
                root2 = root2.right
                root2_changed = True
                root1_changed = False
            else:
                print(root1.data, end=' ')
                root1 = root1.right
                root1_changed = True
                root2_changed = False


        while root1_changed and root1:
            stack1.append(root1)
            root1 = root1.left

        while root2_changed and root2:
            stack2.append(root2)
            root2 = root2.left

    if root1:
        print(root1.data, end=' ')
        root1 = root1.right
    while (root1 or stack1):
        if not root1:
            root1 = stack1.pop()
            print(root1.data, end=' ')
            root1 = root1.right
        else:
            stack1.append(root1)
            root1 = root1.left

    if root2:
        print(root2.data, end=' ')
        root2 = root2.right
    while (root2 or stack2):
        if not root2:
            root2 = stack2.pop()
            print(root2.data, end=' ')
            root2 = root2.right
        else:
            stack2.append(root2)
            root2 = root2.left


def fix_tree(root):
    stack = []
    prev = None
    first = None
    last = None
    while root:
        stack.append(root)
        root = root.left

    while stack:
        root = stack.pop()
        if prev and root.data <= prev.data:
            if not first:
                first = prev
                last = root
            else:
                last = root
        prev = root

        root = root.right
        while root:
            stack.append(root)
            root = root.left

    if first and last:
        first.data, last.data = last.data, first.data


def deepest_node(root=None):
    deepest_node = root
    max_level = -1

    def deepest_node_helper(root=root, level=-1):
        if not root:
            return
        nonlocal deepest_node
        nonlocal max_level
        level += 1
        if level > max_level:
            max_level = level
            deepest_node = root
        deepest_node_helper(root.left, level + 1)
        deepest_node_helper(root.right, level + 1)

    deepest_node_helper(root)
    return deepest_node.data if deepest_node else None


def ceil(root, key):
    if not root:
        return -1
    if root.data == key:
        return root.data
    if root.data > key:
        ceil_from_left = ceil(root.left, key)
        if ceil_from_left < 0:
            return root.data
        return ceil_from_left
    return ceil(root.right, key)


def create_bst_helper(A, start, stop):
    if start > stop:
        return
    mid = (start + stop) // 2
    node = Node(A[mid])
    node.left = create_bst_helper(A, start, mid - 1)
    node.right = create_bst_helper(A, mid + 1, stop)
    return node


def create_balanced_bst(A):
    if not A:
        return
    mid = len(A) // 2
    root = Node(A[mid])
    root.left = create_bst_helper(A, 0, mid - 1)
    root.right = create_bst_helper(A, mid + 1, len(A)-1)
    return root


def create_level_linked_list(root, level_list, level):
    if not root:
        return

    if len(level_list) == level:
        new_list = []
        new_list.append(root)
        level_list.append(new_list)
    else:
        level_list[level].append(root)
    create_level_linked_list(root.left, level_list, level + 1)
    create_level_linked_list(root.right, level_list, level + 1)
    return level_list


def create_level_linked_list_v2(root, level_list):
    curr = []
    if root:
        curr.append(root)
    while curr:
        level_list.append(curr)
        new_list = []
        for parent in curr:
            if parent.left:
                new_list.append(parent.left)
            if parent.right:
                new_list.append(parent.right)
        curr = new_list
    return level_list




root = Node(5)
root.left = Node(4)
root.right = Node(3)
root.left.left = Node(6)
root.right.left = Node(12)
root.right.right = Node(19)


print_tree(root)
print(create_level_linked_list_v2(root, []))
