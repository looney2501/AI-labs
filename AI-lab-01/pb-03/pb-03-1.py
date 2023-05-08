import numpy

"""
    Determines the dot product of two vectors.
    input: two vectors with their coordinates
    output: dot product of the two vectors or None, if the vectors do not have the same dimension
"""


def scalar_product(a, b):
    if len(a) != len(b):
        return None
    return numpy.dot(a, b)


def test_scalar_product():
    assert (scalar_product([2, 3], [2]) is None)
    assert (scalar_product([1], [2]) == 2)
    assert (scalar_product([0, 0, 0], [0, 0, 0]) == 0)
    assert (scalar_product([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4)


test_scalar_product()
