def heapify_iterative(A, i, n=None):
    v = A[i]
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = left
    parent = i

    n = len(A) if not n else n

    while left < n:
        if right < n and A[right] < A[left]:
            smallest = right
        if v <= A[smallest]:
            break
        A[parent] = A[smallest]

        parent = smallest
        left = 2 * smallest + 1
        right = 2 * smallest + 2
        smallest = left

    A[parent] = v
    return A


def heapify_recursive(A, index):
    smallest = index
    left = index * 2 + 1
    right = index * 2 + 2

    if left < len(A) and A[smallest] > A[left]:
        smallest = left
    if right < len(A) and A[smallest] > A[right]:
        smallest = right
    if smallest != index:
        A[index], A[smallest] = A[smallest], A[index]
        heapify_recursive(A, smallest)

    return A


def build_heap(A):
    start = len(A) // 2 - 1
    for i in range(start, -1, -1):
        heapify_iterative(A, i)
    return A


def build_heap_tarnow(A):
    for i in range(1, len(A)):
        parent = (i-1) // 2
        j = i
        v = A[i]
        while parent >= 0 and A[parent] > v:
            A[j] = A[parent]
            j = parent
            parent = (parent - 1) // 2
        A[j] = v
    return A


def heap_sort(A):
    build_heap(A)
    s = []
    while A:
        s.append(A[0])
        A[0] = A[len(A)-1]
        heapify_iterative(A, 0)
        A.pop()

    return s


def check_if_sorted(A):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            return False
    return True


def heap_extract_min(A):
    if not A:
        raise ValueError("Kopiec jest pusty")

    ret = A[0]
    A[0] = A[len(A)-1]
    heapify_iterative(A, 0)
    A.pop()
    return ret


def insert_to_heap(A, v):
    A.append(v)
    j = len(A) - 1
    parent = (j-1) // 2
    while parent >= 0:
        if A[parent] > v:
            A[j] = A[parent]
            j = parent
            parent = (parent - 1) // 2
        else:
            break
    A[j] = v


def heap_delete(A, i):
    A[i] = A[-1]
    A.pop()
    if A and i < len(A):
        heapify_iterative(A, i)
    return A


def heap_sort_for_loop(A):
    build_heap(A)
    result = []
    for i in range(len(A)):
        result.append(A[0])
        A[0] = A[len(A)-i-1]
        heapify_iterative(A, 0, len(A) - i)
    return result