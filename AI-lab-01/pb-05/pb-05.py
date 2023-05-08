"""
    Determines the duplicate number from an array of integers.
    input: an array of n integers from range(1,n) in which only one element is duplicated
    output: the duplicated element
"""


def find_duplicate(numbers):
    max_number = 0
    sum_with_duplicate = 0
    for nr in numbers:
        sum_with_duplicate += nr
        if max_number < nr:
            max_number = nr
    sum_without_duplicate = max_number * (max_number + 1) / 2
    return sum_with_duplicate - sum_without_duplicate


def test_find_duplicate():
    assert (find_duplicate([]) == 0)
    assert (find_duplicate([1, 1]) == 1)
    assert (find_duplicate([1, 3, 2, 2]) == 2)
    assert (find_duplicate([1, 2, 3, 4, 2]) == 2)
    assert (find_duplicate([1, 2, 3, 4, 2]) == 2)
    assert (find_duplicate([1, 3, 3, 4, 2]) == 3)


test_find_duplicate()
