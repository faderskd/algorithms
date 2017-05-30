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



# O(n^2)
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


# O(n*log(n))
def sort_in_wave_form(li):
    li.sort(reverse=True)
    for i in range(1, len(li) - 1, 2):
        li[i], li[i + 1] = li[i + 1], li[i]
    print(li)
    return li


# O(n)
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
    return li


# O(n)
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
    return closest_pair


# O(n)
def closest_pair_from_two_arrays(li1, li2, x):
    merged = []
    fixture = []
    i = j = 0
    while i < len(li1) and j < len(li2):
        if li1[i] < li2[j]:
            merged.append(li1[i])
            fixture.append(1)
            i += 1
        else:
            merged.append(li2[j])
            fixture.append(2)
            j += 1

    while i < len(li1):
        merged.append(li1[i])
        fixture.append(1)
        i += 1

    while j < len(li2):
        merged.append(li2[j])
        fixture.append(2)
        j += 1


    i = 0
    j = len(merged) - 1
    min_diff = abs(merged[i] + merged[j] - x)
    min_i, min_j = i, j
    while i < j:
        diff = abs(merged[i] + merged[j] - x)
        if fixture[i] != fixture[j] and diff < min_diff:
            min_diff = diff
            min_i = i
            min_j = j

        if merged[i] + merged[j] - x > 0:
            j -= 1
        else:
            i += 1

    return merged[min_i], merged[min_j]


# O(n)
def median_of_two_sorted_arrays(A, B):
    counter = 0
    length = len(A) + len(B)
    i = j = 0
    searched_index = length // 2
    curr = prev = None
    while i < len(A) and j < len(B) and counter <= searched_index:
        if A[i] < B[j]:
            prev = curr
            curr = A[i]
            i += 1
        else:
            prev = curr
            curr = B[j]
            j += 1
        counter += 1

    while i < len(A) and counter <= searched_index:
        prev = curr
        curr = A[i]
        counter += 1
        i += 1

    while j < len(B) and counter <= searched_index:
        prev = curr
        curr = B[j]
        counter += 1
        j += 1

    if length % 2 == 0:
        return (curr + prev) / 2
    else:
        return curr

A = [4]
B = [1]
print(sorted(A + B))
print(median_of_two_sorted_arrays(A, B))

