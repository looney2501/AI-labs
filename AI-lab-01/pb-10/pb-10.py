"""
    Find first position of element 1 in a binary array.
    input: binary array, must be sorted
    output: position of the first element equal to 1 or None if the array is empty
"""


def find_first_one(vec):
    if vec is None:
        return None
    n = len(vec)
    if n == 0:
        return None
    left = 0
    right = n
    while right - left >= 1:
        m = (left + right) // 2
        if vec[m] == 0:
            left = m + 1
        else:
            right = m
    return left


"""
    Determines the index of the line from a binary matrix which contains the most number of 1s 
    input: binary matrix with lines sorted 
    output: index of the line which contains the most number of 1s or None if the matrix is empty or if 
            there is no line containing number 1
"""


def line_with_most_ones(matrix):
    if matrix is None:
        return None
    m = len(matrix)
    if m == 0:
        return None
    n = len(matrix[0])
    if n == 0:
        return None
    most_ones = 0
    most_ones_index = -1
    for i in range(m):
        number_of_ones = n - find_first_one(matrix[i])
        if number_of_ones > most_ones:
            most_ones = number_of_ones
            most_ones_index = i
    if most_ones_index == -1:
        return None
    return most_ones_index


def test_line_with_most_ones():
    assert (line_with_most_ones(None) is None)
    assert (line_with_most_ones([]) is None)
    assert (line_with_most_ones([[], []]) is None)
    assert (line_with_most_ones([[0, 0, 0, 1, 1],
                                 [0, 1, 1, 1, 1],
                                 [0, 0, 1, 1, 1]]) == 1)
    assert (line_with_most_ones([[1, 1, 1, 1, 1],
                                 [0, 1, 1, 1, 1],
                                 [0, 0, 1, 1, 1]]) == 0)
    assert (line_with_most_ones([[0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0]]) is None)
    assert (line_with_most_ones([[1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 1]]) == 0)


test_line_with_most_ones()
