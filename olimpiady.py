def get_sum(start, stop, li):
    s = 0
    for i in range(start, stop + 1):
        s += li[i]
    return s


def grzybiarz(li, m, k):
    max_sum = 0
    # go to left
    for i in range(min(m, k) + 1):
        max_sum = max(get_sum(k - i, min(max(k, k + m - 2 * i), len(li) - 1), li), max_sum)

    for i in range(min(len(li) - k, m)):
        max_sum = max(get_sum(max(0, min(k - (m - 2 * i), k)), k + i, li), max_sum)
    return max_sum

# print(grzybiarz([2, 3, 7, 5, 1, 3, 9], 6, 4))

def kolejka_w_sklepie(queue):
    begin_persons = 0
    persons = 0
    for p in queue:
        if p == 0:
            persons += 1
        else:
            persons -= 1
        if persons < 0:
            begin_persons += 1
            persons = 0
    return begin_persons

print(kolejka_w_sklepie([1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1]))