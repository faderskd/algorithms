import sys


# O(n*k)
def merge_lists(lists):
    l = len(lists)
    counters = [0] * l
    result = []
    n = sum(len(li) for li in lists)

    for i in range(n):
        min_v = sys.maxsize
        min_counter_index = -1

        for j in range(l):
            if counters[j] < len(lists[j]) and lists[j][counters[j]] < min_v:
                min_v = lists[j][counters[j]]
                min_counter_index = j
        result.append(min_v)
        counters[min_counter_index] += 1

    return result


# O(n*log(k))
def merge_min_heap(lists):
    import heapq

    l = len(lists)
    counters = [0] * l
    result = []
    n = sum(len(li) for li in lists)
    heap = [(li[0], counters_index) for (counters_index, li) in enumerate(lists) if li]
    heapq.heapify(heap)

    for i in range(n):
        v, counters_index = heapq.heappop(heap)
        result.append(v)
        counters[counters_index] += 1
        if counters[counters_index] < len(lists[counters_index]):
            heapq.heappush(heap, (lists[counters_index][counters[counters_index]], counters_index))

    return result

print(merge_min_heap([[], [], [1, 3]]))