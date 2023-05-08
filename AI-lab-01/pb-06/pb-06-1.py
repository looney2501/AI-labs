"""
    Determines the majority element from an array of numbers
    input: an array of numbers with its length = n
    output: the element which appears more than n/2 times or None if there is no majority element
"""


def majority_winner(numbers):
    if numbers is None:
        return None
    freq_map = {}
    for nr in numbers:
        if nr in freq_map:
            freq_map[nr] += 1
        else:
            freq_map[nr] = 1
    majority_candidate = max(freq_map, key=freq_map.get)
    if freq_map[majority_candidate] > len(numbers) / 2:
        return majority_candidate
    return None

def test_majority_winner():
    assert (majority_winner(None) is None)
    assert (majority_winner([1]) == 1)
    assert (majority_winner([1, 1, 2]) == 1)
    assert (majority_winner([1, 1, 2, 2]) is None)
    assert (majority_winner([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2)
    assert (majority_winner([1, 2, 3, 4]) is None)


test_majority_winner()


