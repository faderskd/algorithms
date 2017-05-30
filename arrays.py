def find_duplicates(array):
    c = 0
    i = 0
    while i < len(array):
        c += 1
        if array[i] in [i, -1, None]:
            i += 1
        else:
            if array[array[i]] in [array[i], -1]:
                array[array[i]] = -1
                array[i] = None
            else:
                array[array[i]], array[i], = array[i], array[array[i]]

    return [i for i in range(len(array)) if array[i] == -1]


def sort_after_square(li):
    i = 0
    j = len(li) - 1
    res = [0] * len(li)
    c = 1
    while i <= j:
        if abs(li[i]) > li[j]:
            res[len(li) - c] = li[i]**2
            i += 1
        else:
            res[len(li) - c] = li[j]**2
            j -= 1
        c += 1
    return res


def max_k_subarray(li, k):
    if k > len(li):
        raise ValueError('k grater than list')
    max_s = s = sum(li[0: k])
    for i in range(k, len(li)):
        s -= li[i - k]
        s += li[i]
        max_s = max(s, max_s)
    return max_s


def minimum_swaps(li):
    counter = 0
    for i in range(1, len(li)):
        if (li[i] - 1) - i > 2:
            return -1
        j = i - 1
        v = li[i]
        c = 0
        while j >= 0 and li[j] > v and c < 2:
            counter += 1
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = v
    return counter


def swap_to_equal_sum(A, B, m):
    diff = sum(A) - sum(B)
    if diff % 2 != 0:
        return
    diff /= 2
    diff = int(diff)
    counters = [0]*(m + 1)
    for i in range(len(B)):
        counters[B[i]] += 1
    for i in range(len(A)):
        if A[i] - diff >= 0 and A[i] - diff <= m and counters[A[i] - diff] > 0:
            print(A[i], A[i] - diff)
            return


def find_last_one(li, start, end):
    if start <= end:
        middle = (start + end) // 2
        if middle == end and li[middle] == 1:
            return 1 + middle
        if li[middle] == 1 and li[middle + 1] == 0:
            return 1 + middle
        if li[middle] == 0:
            return find_last_one(li, start, middle - 1)
        return find_last_one(li, middle + 1, end)
    return 0


def find_two(even_counters):
    max_even = second_max_even = 0
    for i in range(1, len(even_counters)):
        if even_counters[i] > even_counters[max_even]:
            second_max_even = max_even
            max_even = i
        elif max_even == second_max_even or even_counters[i] > even_counters[second_max_even]:
            second_max_even = i
    return (even_counters[max_even], even_counters[second_max_even])


def crossing_over_point(li, x):
    start = 0
    stop = len(li) - 1

    while start <= stop:
        middle = (start + stop) // 2
        if middle == stop and li[middle] == x:
            return middle
        if li[middle] == x and x < li[middle + 1]:
            return middle
        if li[middle] <= x:
            start = middle + 1
        else:
            stop = middle - 1
    return -1


def find_shifted_starting_point(li):
    start = 0
    stop = len(li) - 1

    while start < stop:
        middle = (start + stop) // 2
        if li[middle] > li[middle + 1]:
            return middle
        if middle - 1 >= start and li[middle - 1] > li[middle]:
            return middle - 1
        if li[middle] < li[start]:
            stop = middle - 1
        elif li[middle] > li[stop]:
            start = middle + 1
        else:
            break
    return -1


def find_in_shifted(li, x):
    index = find_shifted_starting_point(li)
    if (index == -1):
        start, stop = 0, len(li) - 1
    if li[-1] < x:
        start, stop = 0, index
    elif li[-1] >= x:
        start, stop = index + 1, len(li) - 1

    while start <= stop:
        middle = (start + stop) // 2
        if li[middle] == x:
            return middle
        if li[middle] > x:
            stop = middle - 1
        else:
            start = middle + 1
    return -1


def merge_not_filled(A, B):
    i = j = len(A) - 1
    while i >= 0:
        if A[j] != None:
            j -= 1
            i = j
            continue
        if A[i] != None:
            A[i], A[j] = A[j], A[i]
        i -= 1

    i = len(B)
    j = k = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            A[k] = A[i]
            i += 1
        else:
            A[k] = B[j]
            j += 1
        k += 1

    while j < len(B):
        A[k] = B[j]
        j += 1
        k += 1

    return A


def set_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    r, c = False, False

    for i in range(cols):
        if matrix[0][i] == 0:
            r = True
    for i in range(rows):
        if matrix[i][0] == 0:
            c = True

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if r:
        for i in range(cols):
            matrix[0][i] = 0
    if c:
        for i in range(rows):
            matrix[i][0] = 0
    return matrix


def merge_two_in_place(A, B):
    i = len(A) - len(B) - 1
    j = len(B) - 1
    k = len(A) - 1
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1

    while j >= 0:
        A[k] = B[j]
        j -= 1
        k -= 1
    return A


def rotate_matrix(matrix):
    N = len(matrix)
    layers = len(matrix) // 2
    for i in range(layers):
        for j in range(N - 1 - 2*i):
            matrix[j + i][i], matrix[N - 1 - i][j + i] = matrix[N - 1 - i][j + i], matrix[j + i][i]
            matrix[N - 1 - i][j + i], matrix[N - 1 - i - j][N - 1 - i] = matrix[N - 1 - i - j][N - 1 - i], matrix[N - 1 - i][j + i]
            matrix[N - 1 - i - j][N - 1 - i], matrix[i][N - 1 - i - j] = matrix[i][N - 1 - i - j], matrix[N - 1 - i - j][N - 1 - i]
    return matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()


def max_no_adjacent_subarray(array):
    sum_with_prev = 0
    sum_without_prev = 0
    max_sum = 0
    for curr in array:
        tmp_sum_with_prev = sum_with_prev
        sum_with_prev = sum_without_prev + curr
        max_sum = max(max_sum, sum_with_prev)
        sum_without_prev = max(sum_without_prev, tmp_sum_with_prev)
    return max_sum


def check_majority(li, x):
    last_index = len(li) // 2 if len(li) % 2 == 0 else len(li) // 2 + 1
    for i in range(last_index):
        if li[i] == x and li[i + len(li) // 2] == x:
            return True
    return False

print(check_majority([1, 2, 2, 2, 3], 2))