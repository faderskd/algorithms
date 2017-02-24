from collections import Counter


def maximum_frequency(li):
    c = Counter(li)
    sorted_keys = sorted(c)

    min_freq = len(li)
    max_diff = 0
    for k in sorted_keys:
        curr_freq = c[k]
        max_diff = max(max_diff, curr_freq - min_freq)
        min_freq = min(min_freq, curr_freq)
    return max_diff


print(maximum_frequency([3, 1, 3, 2, 3, 2]))