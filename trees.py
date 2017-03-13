class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


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
        else:
            if not curr.right:
                curr.right = Node(x)
                break
            curr = curr.right
    return root_copy


def insert_to_tree_recursive(root, x):
    if not root:
        return Node(x)

    if root.data > x:
        root.left = insert_to_tree_recursive(root.left, x)
    else:
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
    print(' ')
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
    if not root.left:
        return root
    return find_inorder_successor(root.left)


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

