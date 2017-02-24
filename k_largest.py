# O(k*(n-k))
def k_largest(li, k):
    for i in range(k):
        max_v = li[i]
        for j in range(k, len(li)):
            if max_v < li[j]:
                max_v = li[j]
                li[j], li[i] = li[i], li[j]
    return li[0: k]


def bubble_k_largest(li, k):
    for i in range(k):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li[len(li) - k: len(li)]


def find_min_index(li):
    index = 0
    for i in range(1, len(li)):
        if li[index] > li[i]:
            index = i
    return index


# O(k*(n-k))
def tmp_table_k_largest(li, k):
    tmp = li[0: k]

    for i in range(k, len(li)):
        min_index = find_min_index(tmp)
        if li[i] > tmp[min_index]:
            tmp[min_index] = li[i]
    return tmp


# O(k + (n - k)*log(k))
from min_heap import build_heap, heapify_iterative

def heap_k_largest(li, k):
    heap = li[0: k]
    build_heap(heap)
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            heapify_iterative(heap, 0)
    return heap


print(heap_k_largest([6, 1, 0, -1, 5, 3, 7, 0, 1, 9, 8], 3))
