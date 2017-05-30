# O(n*log(n))
def find_leader_sorted(A):
    A.sort()
    leader = A[0]
    max_times = 1
    tmp_times = 1
    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            tmp_times = 1
        else:
            tmp_times += 1
        if tmp_times > max_times:
            leader = A[i]
            max_times = tmp_times
    return leader if max_times > len(A) // 2 else "Brak"

# O(n)
def find_leader(A):
    tmp_times = 0
    prev = None
    for a in A:
        if tmp_times == 0:
            tmp_times = 1
            prev = a
        else:
            if prev == a:
                tmp_times += 1
            else:
                tmp_times -= 1

    count = 0
    for a in A:
        if a == prev:
            count += 1
    return prev if count > len(A) // 2 else "Brak"

# A = list(map(int, input().split()))

# print(find_leader(A))

