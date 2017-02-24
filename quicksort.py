import random
from max_heap import check_if_sorted


def partition_horae(A, p, r):
    v = A[p]
    i = p - 1
    j = r + 1

    while True:
        i += 1
        j -= 1

        while A[i] < v:
            i += 1
        while A[j] > v:
            j -= 1

        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]


def partition_left(A, p, r):
    v = A[p]
    i = p
    j = r

    while True:
        while i < r and A[i] <= v:
            i += 1

        while j > p and A[j] >= v:
            j -= 1

        if j > i:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        else:
            A[p], A[j] = A[j], A[p]
            return j


def partition_tarnow(A, p, r):
    center = (r + p) // 2
    A[center], A[r] = A[r], A[center]
    pivot = A[r]
    j = p

    for i in range(p, r):
        if A[i] <= pivot:
            A[j], A[i] = A[i], A[j]
            j += 1
    A[r], A[j] = A[j], A[r]
    return j


def partition_equal_in_center(A, p, r):
    center = p
    A[center], A[r] = A[r], A[center]
    pivot = A[r]
    j = p

    for i in range(p, r):
        if A[i] < pivot:
            A[j], A[i] = A[i], A[j]
            j += 1
    A[r], A[j] = A[j], A[r]

    k = j
    for i in range(j + 1, r + 1):
        if A[i] == pivot:
            A[k+1], A[i] = A[i], A[k+1]
            k += 1

    return (j, k)


def quicksort(A, p, r):
    if r > p:
        q = partition_tarnow(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    return A


def tail_recursive_quicksort(A, p, r):
    while r > p:
        q = partition_tarnow(A, p, r)
        if q < (p + r) // 2:
            tail_recursive_quicksort(A, p, q - 1)
            p = q + 1
        else:
            tail_recursive_quicksort(A, q + 1, r)
            r = q - 1
    return A


def quicksort_ommit_equal(A, p, r):
    if r > p:
        q = partition_equal_in_center(A, p, r)
        quicksort_ommit_equal(A, p, q[0] - 1)
        quicksort_ommit_equal(A, q[1] + 1, r)
    return A


A = [4, 4, 4, 4, 4, 4]
print(partition_tarnow(A, 0, len(A)-1))
print(A)
