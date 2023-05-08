"""
    Determines the majority element from an array of numbers
    input: an array of numbers with its length = n
    output: the element which appears more than n/2 times or None if there is no majority element
"""


def majority_winner(numbers):
    if numbers is None:
        return None
    n = len(numbers)
    if n == 0:
        return None
    if n == 1:
        return numbers[0]
    candidate = numbers[0]
    freq = 1
    for i in range(1, n):
        if numbers[i] == candidate:
            freq += 1
        else:
            freq -= 1
            if freq == 0:
                candidate = numbers[i]
                freq = 1
    if freq > n / 2:
        return candidate
    freq = 0
    for el in numbers:
        if el == candidate:
            freq += 1
    if freq > n / 2:
        return candidate
    return None


def test_majority_winner():
    assert (majority_winner(None) is None)
    assert (majority_winner([1]) == 1)
    assert (majority_winner([1, 1, 2]) == 1)
    assert (majority_winner([1, 1, 2, 2]) is None)
    assert (majority_winner([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2)
    assert (majority_winner([1, 2, 3, 4]) is None)


test_majority_winner()
