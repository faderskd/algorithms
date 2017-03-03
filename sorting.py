import sys

# O(n*log(n))
def minimum_length_unsorted_array(li):
    tmp_li = li[:]
    tmp_li.sort()
    end = -1
    start = -1
    for i in range(len(li)):
        if li[i] != tmp_li[i]:
            if start < 0:
                start = i
            end = i
    return end - start + 1 if start > 0 else 0

# O(n)
def minimum_length_unsorted_array_linear(li):
    start = end = -1
    local_max = -sys.maxsize
    local_min = sys.maxsize
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            local_min = min(local_min, li[i + 1])
            local_max = max(local_max, li[i])

    for i in range(len(li)):
        if start < 0 and local_min < li[i]:
            start = i
        if local_max > li[i]:
            end = i

    return (start, end)


# O(n)
def find_closest_elements(li, x, k):
    try:
        index = li.index(x)
    except ValueError:
        return []

    i = index - 1
    j = index + 1
    counter = 0
    while counter < k and i >= 0 and j < len(li):
        if li[index] - li[i] < li[index] - li[j]:
            i -= 1
        else:
            j += 1
        counter += 1

    while counter < k and i >= 0:
        i -= 1
        counter += 1

    while counter < k and j < len(li):
        j += 1
        counter += 1
    return li[i + 1: index] + li[index + 1: j]


# A[0.....i] <= x < A[i+1...n]
def find_crossover_point(A, x, low, high):
    if x >= A[high]:
        return high
    if x < A[low]:
        return low

    mid = (low + high) // 2
    if A[mid] <= x and A[mid + 1] > x:
        return mid
    elif A[mid] <= x:
        return find_crossover_point(A, x, mid + 1, high)
    else:
        return find_crossover_point(A, x, low, mid - 1)

A = [1,2]
print(find_crossover_point(A, 3, 0, len(A)-1))


