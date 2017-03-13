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

print(sort_after_square([-5, -4, -2, -1, 0, 0, 0]))


