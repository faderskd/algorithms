def maximum_subarray(A):
    max_sum = tmp_sum = A[0]
    max_index_start = 0
    max_index_stop = 0
    tmp_index_start = 0

    for i in range(1, len(A)):
        if tmp_sum + A[i] > A[i]:
            tmp_sum = tmp_sum + A[i]
        else:
            tmp_sum = A[i]
            tmp_index_start = i

        if tmp_sum > max_sum:
            max_sum = tmp_sum
            max_index_start = tmp_index_start
            max_index_stop = i

    return max_index_start, max_index_stop, max_sum


def brute_force_maximum_subarray(A):
    max_sum = A[0]
    max_index_start = 0
    max_index_stop = 0

    for i in range(len(A)):
        tmp_sum = 0
        for j in range(i, len(A)):
            tmp_sum += A[j]
            if tmp_sum > max_sum:
                max_index_start = i
                max_index_stop = j
                max_sum = tmp_sum

    return (max_index_start, max_index_stop, max_sum)


def max_subarray_modified(A):
    max_sum = A[0]
    tmp_sum = A[0]
    for i in range(1, len(A)):
        if tmp_sum <= 0:
            tmp_sum = A[i]
        else:
            tmp_sum = tmp_sum + A[i]

        max_sum = max(tmp_sum, max_sum)
    return max_sum