"""
    Determines the partial sums of a matrix
    input: matrix of numbers
    output: matrix of partial sums
"""


def generate_partial_sums(matrix):
    if matrix is None:
        return None
    m = len(matrix) + 1
    n = len(matrix[0]) + 1
    partial_sums = [[0 for j in range(n)] for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            partial_sums[i][j] = partial_sums[i - 1][j] + partial_sums[i][j - 1] - partial_sums[i - 1][j - 1] + \
                                 matrix[i - 1][j - 1]
    return [partial_sums[i][1:m] for i in range(1, n)]


"""
    Calculates the sums of elements inside sub-matrices determined by pairs of coordinates.
    input: list of pairs of coordinates
    outpus: list of integers representing the sums of the sub-matrices
"""


def calculate_partial_sums(matrix, pairs):
    partial_sums = generate_partial_sums(matrix)
    sums = []
    for pair in pairs:
        x1 = pair[0][0]
        y1 = pair[0][1]
        x2 = pair[1][0]
        y2 = pair[1][1]
        current_sum = partial_sums[x2][y2]
        line_before = False
        column_before = False
        if x1 - 1 >= 0:
            line_before = True
            current_sum -= partial_sums[x1 - 1][y2]
        if y1 - 1 >= 0:
            column_before = True
            current_sum -= partial_sums[x2][y1 - 1]
        if line_before and column_before:
            current_sum += partial_sums[x1 - 1][y1 - 1]
        sums.append(current_sum)
    return sums


def test_calculate_partial_sums():
    assert (calculate_partial_sums([[0, 2, 5, 4, 1],
                                    [4, 8, 2, 3, 7],
                                    [6, 3, 4, 6, 2],
                                    [7, 3, 1, 8, 3],
                                    [1, 5, 7, 9, 4]], [[[1, 1], [3, 3]], [[2, 2], [4, 4]]]) == [38, 44])
    assert (calculate_partial_sums([[0, 2, 5, 4, 1],
                                    [4, 8, 2, 3, 7],
                                    [6, 3, 4, 6, 2],
                                    [7, 3, 1, 8, 3],
                                    [1, 5, 7, 9, 4]], [[[0, 0], [3, 3]], [[2, 2], [4, 4]]]) == [66, 44])
    assert (calculate_partial_sums([[0, 2, 5, 4, 1],
                                    [4, 8, 2, 3, 7],
                                    [6, 3, 4, 6, 2],
                                    [7, 3, 1, 8, 3],
                                    [1, 5, 7, 9, 4]], [[[0, 1], [3, 3]], [[2, 2], [4, 4]]]) == [49, 44])
    assert (calculate_partial_sums([[0, 2, 5, 4, 1],
                                    [4, 8, 2, 3, 7],
                                    [6, 3, 4, 6, 2],
                                    [7, 3, 1, 8, 3],
                                    [1, 5, 7, 9, 4]], [[[1, 0], [3, 3]], [[2, 2], [4, 4]]]) == [55, 44])


test_calculate_partial_sums()
