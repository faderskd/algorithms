import sys

def find_maximum_crossing_subarray(A, low, mid, high):
    max_left_sum = -sys.maxsize
    left_sum = 0
    max_left_i = -1
    for i in range(mid, low - 1, -1):
        left_sum += A[i]
        if left_sum > max_left_sum:
            max_left_sum = left_sum
            max_left_i = i

    max_right_sum = -sys.maxsize
    right_sum = 0
    max_right_i = -1
    for i in range(mid + 1, high + 1):
        right_sum += A[i]
        if right_sum > max_right_sum:
            max_right_sum = right_sum
            max_right_i = i

    return max_left_i, max_right_i, max_left_sum + max_right_sum


def maximum_subarray(A, low, high):
    if high == low:
        return low, high, A[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = maximum_subarray(A, low, mid)
    right_low, right_high, right_sum = maximum_subarray(A, mid + 1, high)
    mid_low, mid_high, mid_sum = find_maximum_crossing_subarray(A, low, mid, high)

    if left_sum >= mid_sum and left_sum >= right_sum:
        return left_low, left_high, left_sum
    elif right_sum >= mid_sum and right_sum >= left_sum:
        return right_low, right_high, right_sum
    else:
        return mid_low, mid_high, mid_sum


# Strassen's alghoritm for multiplying matrices

def add_matrices(A, B):
    if not (A and B and len(A[0]) == len(B[0])):
        raise ValueError('Dimensions of matrices incorrect')

    C = [[0 for i in A[0]] for i in A]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract_matrices(A, B):
    if not (A and B and len(A[0]) == len(B[0])):
        raise ValueError('Dimensions of matrices incorrect')

    C = [[0 for i in A[0]] for i in A]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C


def multiply_square_matrix(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]

    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
        return C

    middle = n // 2

    a11 = [[A[i][j] for j in range(middle)] for i in range(middle)]
    a12 = [[A[i][j] for j in range(middle, n)] for i in range(middle)]
    a21 = [[A[i][j] for j in range(middle)] for i in range(middle, n)]
    a22 = [[A[i][j] for j in range(middle, n)] for i in range(middle, n)]

    b11 = [[B[i][j] for j in range(middle)] for i in range(middle)]
    b12 = [[B[i][j] for j in range(middle, n)] for i in range(middle)]
    b21 = [[B[i][j] for j in range(middle)] for i in range(middle, n)]
    b22 = [[B[i][j] for j in range(middle, n)] for i in range(middle, n)]

    c11 = add_matrices(multiply_square_matrix(a11, b11, middle), multiply_square_matrix(a12, b21, middle))
    c12 = add_matrices(multiply_square_matrix(a11, b12, middle), multiply_square_matrix(a12, b22, middle))
    c21 = add_matrices(multiply_square_matrix(a21, b11, middle), multiply_square_matrix(a22, b21, middle))
    c22 = add_matrices(multiply_square_matrix(a21, b12, middle), multiply_square_matrix(a22, b22, middle))

    for i in range(middle):
        for j in range(middle):
            C[i][j] = c11[i][j]
            C[i][j + middle] = c12[i][j]
            C[i + middle][j] = c21[i][j]
            C[i + middle][j + middle] = c22[i][j]

    return C

A = [[1, 3], [2, 4]]
B = [[5, 4], [1, 2]]
print(multiply_square_matrix(A, B, 2))
