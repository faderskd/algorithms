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
    if not li:
        return []

    index = 0
    for i in range(len(li)):
        if li[i] <= x:
            index = i

    i = index
    j = index + 1
    if li[index] == x:
        i -= 1

    counter = 0
    while counter < k and i >= 0 and j < len(li):
        if li[index] - li[i] < li[j] - li[index]:
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

    return li[i + 1: index] + li[index + 1 if li[index] == x else index: j]


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


# O(log(n) + k) TODO
def optimized_find_closes_elements(li, x, k):
    index = find_closest_elements(li, x, k)
    if li[index]:
        index -= 1

# A = [1, 3, 5, 5, 6, 6, 6, 7]
# print(find_closest_elements(A, 8, 2))


def find_zero_triplets(li):
    li.sort()
    for i in range(len(li) - 2):
        l = i + 1
        r = len(li) - 1
        while l < r:
            s = li[i] + li[l] + li[r]
            if s == 0:
                print(li[i], li[l], li[r])
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1


def sort_in_wave_form(li):
    li.sort(reverse=True)
    for i in range(1, len(li) - 1, 2):
        li[i], li[i + 1] = li[i + 1], li[i]
    print(li)
    return li


def sort_in_wave_form_linear(li):
    if len(li) < 3:
        return li
    if li[0] < li[1]:
        li[1], li[0] = li[0], li[1]
    for i in range(2, len(li) - 2, 2):
        if li[i - 1] > li[i]:
            li[i - 1], li[i] = li[i], li[i - 1]
        if li[i + 1] > li[i]:
            li[i + 1], li[i] = li[i], li[i + 1]
    if li[-1] < li[-2]:
        li[-1], li[-2] = li[-2], li[-1]
    print(li)
    return li


def closes_pair_sum(li, x):
    li.sort()
    closest_pair = li[0], li[1]
    r = len(li) - 1
    l = 0
    while l < r:
        diff = li[l] + li[r] - x
        if abs(diff) < abs(closest_pair[0] + closest_pair[1] - x):
            closest_pair = li[l], li[r]
        if diff > 0:
            r -= 1
        elif diff < 0:
            l += 1
        else:
            break
    print(closest_pair)
    return closest_pair


closes_pair_sum([-5, -2, -2, 0, 4, 6, 12, 13, 14], 5)