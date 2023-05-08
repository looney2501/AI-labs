from heapq import heapify, heappushpop, heappush, heappop

"""
    Determine the k largest element of an array of numbers
    input:  numbers - array of numbers
            k - integer
    output: the k largest element of the array of numbers, or None if k >= length of the array
"""


def get_k_max(numbers, k):
    if numbers is None or k is None:
        return None
    n = len(numbers)
    if n == 0:
        return None
    if k > n:
        return None
    heap = []
    heapify(heap)
    for i in range(k):
        heappush(heap, numbers[i])
    for i in range(k, n):
        if numbers[i] > heap[0]:
            heappushpop(heap, numbers[i])
    return heap[0]


def test_k_max():
    assert (get_k_max(None, 1) is None)
    assert (get_k_max([1], None) is None)
    assert (get_k_max([], 3) is None)
    assert (get_k_max([1, 2], 3) is None)
    assert (get_k_max([1, 2, 3], 3) == 1)
    assert (get_k_max([7, 4, 6, 3, 9, 1], 2) == 7)
    assert (get_k_max([7, 4, 6, 3, 9, 1], 4) == 4)


test_k_max()
