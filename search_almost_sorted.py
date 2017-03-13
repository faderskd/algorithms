def search_in_almost_sorted(li, x):
    start = 0
    end = len(li) - 1
    while end >= start:
        mid = (start + end) // 2
        if li[mid] == x:
            return mid
        if mid < end and li[mid + 1] == x:
            return mid + 1
        if mid > start and li[mid - 1] == x:
            return mid - 1

        if li[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return -1
