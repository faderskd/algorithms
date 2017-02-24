def heapify_iterative(A, i):
    v = A[i]
    left = 2 * i + 1
    right = 2 * i + 2
    largest = left
    parent = i

    while left < len(A):
        if right < len(A) and A[right] > A[left]:
            largest = right
        if v >= A[largest]:
            break
        A[parent] = A[largest]

        parent = largest
        left = 2*largest + 1
        right = 2*largest + 2
        largest = left

    A[parent] = v
    return A


def heapify_recursive(A, index):
    largest = index
    left = index * 2 + 1
    right = index * 2 + 2

    if left < len(A) and A[largest] < A[left]:
        largest = left
    if right < len(A) and A[largest] < A[right]:
        largest = right
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        heapify_recursive(A, largest)

    return A


def build_heap(A):
    start = len(A) // 2 - 1
    for i in range(start, -1, -1):
        heapify_iterative(A, i)
    return A


def build_heap_tarnow(A):
    for i in range(1, len(A)):
        parent = (i - 1) // 2
        j = i
        v = A[i]
        while parent >= 0 and A[parent] < v:
            A[j] = A[parent]
            j = parent
            parent = (parent - 1) // 2
        A[j] = v
    return A


def heap_sort(A):
    build_heap(A)
    s = [0] * len(A)
    while A:
        s[len(A) - 1] = A[0]
        A[0] = A[len(A) - 1]
        heapify_iterative(A, 0)
        A.pop()

    return s


def heap_sort_tarnow(A):
    build_heap_tarnow(A)

    s = [0] * len(A)
    for i in range(len(A) - 1):
        length = len(A) - i
        s[length - 1] = A[0]
        v = A[length - 1]
        parent = 0
        left = largest = 1
        right = 2

        while left < length:
            if right < length and A[right] > A[left]:
                largest = right
            if A[largest] < v:
                break

            A[parent] = A[largest]

            parent = largest
            left = largest = 2 * parent + 1
            right = 2 * parent + 2

        A[parent] = v

    if A:
        s[0] = A[0]
    return s


def check_if_sorted(A):
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            return False
    return True


def heap_extract_max(A):
    if not A:
        raise ValueError("Kopiec jest pusty")

    ret = A[0]
    A[0] = A[len(A) - 1]
    heapify_iterative(A, 0)
    A.pop()
    return ret


def insert_to_heap(A, v):
    A.append(v)
    j = len(A) - 1
    parent = (j - 1) // 2
    while parent >= 0 and A[parent] < v:
        A[j] = A[parent]
        j = parent
        parent = (parent - 1) // 2
    A[j] = v


def increase_key(A, i, k):
    max_n = max(A[i], k)
    parent = (i - 1) // 2
    j = i
    while parent >= 0 and A[parent] < max_n:
        A[j] = A[parent]
        j = parent
        parent = (j - 1) // 2
    A[j] = max_n


def heap_delete(A, i):
    A[i] = A[-1]
    A.pop()
    if A and i < len(A):
        heapify_iterative(A, i)
    return A