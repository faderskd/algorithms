import math

# finds minimum value in range(a, b) from list li in O(1) time
def preprocess(li):
    matrix = [[0 for i in li] for j in li]
    for i in range(len(li)):
        for j in range(i, len(li)):
            matrix[i][j] = min(li[i:j + 1])
    return matrix


def range_minimum_query(matrix, a, b):
    if a > b:
        raise ValueError('Bad range vaules')
    return matrix[a][b]


# finds minimum value using O(sqrt(n)) time
def sqrt_square_root_decomposition(li):
    block_size = int(math.sqrt(len(li)))
    result = []

    i = 0
    while (i + 1) * block_size <= len(li):
        result.append(min(li[block_size * i: block_size * (i + 1)]))
        i += 1
    return result


def range_minimum_square_root(li, processed, l, r):
    block_size = int(math.sqrt(len(li)))
    min_e = li[l]

    while l != 0 and l % block_size != 0 and l <= r:
        min_e = min(min_e, li[l])
        l += 1

    i = l // block_size
    while (i + 1) * block_size - 1 <= r:
        min_e = min(min_e, processed[i])
        l += block_size
        i += 1

    while l <= r:
        min_e = min(min_e, li[l])
        l += 1

    return min_e

li = [0, 1, 2, 3, 4]
processed = sqrt_square_root_decomposition(li)
print(processed)
print(range_minimum_square_root(li, processed, 3, 4))
