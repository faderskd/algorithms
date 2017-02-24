import sys


def find_max_k_element(A, k):
    if k < 1:
        return None

    MAX_INT = sys.maxsize
    MIN_INT = -sys.maxsize

    M = [MIN_INT]*k + [MAX_INT]

    for a in A:
        j = -1
        while a > M[j+1]:
            j += 1
            M[j] = M[j+1]
        if j >= 0:
            M[j] = a
    return M[0]

A = [3, 1]

print(find_max_k_element(A, 2))
