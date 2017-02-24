import heapq

# sorts array at O(k + (n-k)*log(k)) when k is max length from source to target index of unsorted element
def sort_almost_sorted(A, k):
    heap = A[0: k + 1]
    heapq.heapify(heap)
    result = []
    for i in range(len(A) - (k + 1)):
        result.append(heapq.heapreplace(heap, A[k + 1 + i]))

    for i in range(k + 1):
        result.append(heapq.heappop(heap))
    return result

A = [6,5,4,3,1,2]
print(sort_almost_sorted(A, 5))