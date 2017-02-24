def counting_sort_by_digits(A, digit):
    length = len(A)
    result = [0] * length
    counters = [0] * 10

    for n in A:
        counters[int((n // digit)) % 10] += 1

    for i in range(1, 10):
        counters[i] += counters[i - 1]

    for i in range(length - 1, -1, -1):
        index = int((A[i] // digit)) % 10
        result[counters[index] - 1] = A[i]
        counters[index] -= 1

    for i in range(length):
        A[i] = result[i]


def radix_sort(A):
    max_n = max(A)
    digit = 1
    while int(max_n) > 0:
        counting_sort_by_digits(A, digit)
        digit *= 10
        max_n /= digit
    return A


def counting_sort(A):
    min_a = min(A)
    max_a = max(A)
    result = [0] * len(A)
    counters = [0] * (max_a - min_a + 1)

    for i in range(len(A)):
        counters[A[i] - min_a] += 1

    for i in range(1, len(counters)):
        counters[i] += counters[i - 1]

    for i in range(len(A) - 1, -1, -1):
        index = A[i] - min_a
        result[counters[index] - 1] = A[i]
        counters[index] -= 1
    return result


def bucket_sort(A):
    buckets = [[] for _ in A]
    for a in A:
        buckets[int(a*len(A))].append(a)

    for b in buckets:
        b.sort()

    result = []
    for b in buckets:
        result.extend(b)
    return result


A = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.999]
print(bucket_sort(A))
