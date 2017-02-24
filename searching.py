import math


# O(sqrt(n))
def jump_search(A, v):
    block_size = int(math.sqrt(len(A)))
    start = 0
    end = min(len(A), start + block_size) - 1
    while A[end] < v:
        start += block_size
        if start >= len(A):
            return -1
        end = min(len(A), start + block_size) - 1

    while start <= end:
        if A[start] == v:
            return start
        start += 1

    return -1


# O(log(log(n)))
def interpolation_search(A, v):
    start = 0
    end = len(A) - 1
    while start <= end and A[start] <= v < A[end]:
        index = int(((v - A[start]) / (A[end] - A[start])) * (end - start)) + start

        if A[index] == v:
            return index
        elif A[index] > v:
            end = index - 1
        else:
            start = index + 1

    if A[end] == v:
        return end

    return -1