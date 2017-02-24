def insert_to_heap(A, d, v):
    A.append(v)
    j = len(A) - 1
    parent = (j - 1) // d
    while parent >= 0 and A[parent] < v:
        A[j] = A[parent]
        j = parent
        parent = (parent - 1) // d
    A[j] = v


def extract_max(A, d):
    ret = A[0]
    A[0] = v = A[-1]
    A.pop()
    parent = 0
    largest = 1

    while largest < len(A):
        for i in range(2, d+1):
            if d * parent + i < len(A) and A[largest] < A[d*parent+i]:
                largest = d * parent + i

        if A[largest] <= v:
            break
        A[parent] = A[largest]
        parent = largest
        largest = parent * d + 1

    if A:
        A[parent] = v

    return ret