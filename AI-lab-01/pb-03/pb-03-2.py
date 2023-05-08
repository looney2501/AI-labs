"""
    Determines the dot product of two vectors.
    input: two vectors with their coordinates
    output: dot product of the two vectors or None, if the vectors do not have the same dimension
"""


def scalar_product(a, b):
    if len(a) != len(b):
        return None
    product = 0
    for i in range(len(a)):
        if a[i] != 0 and b[i] != 0:
            product += a[i]*b[i]
    return product


def test_scalar_product():
    assert (scalar_product([2, 3], [2]) is None)
    assert (scalar_product([1], [2]) == 2)
    assert (scalar_product([0, 0, 0], [0, 0, 0]) == 0)
    assert (scalar_product([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4)


test_scalar_product()