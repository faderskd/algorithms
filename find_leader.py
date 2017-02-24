def find_leader(A):
    curr_leader_count = 0
    leader = None

    for a in A:
        if leader:
            if a == leader:
                curr_leader_count += 1
            elif curr_leader_count > 1:
                curr_leader_count -= 1
            else:
                curr_leader_count = 0
                leader = None
        else:
            leader = a

    return leader if leader and A.count(leader) > len(A) // 2 else None

A = list(map(int, input().split()))

print(find_leader(A))