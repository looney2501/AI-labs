import math

"""
    Determine the Euclidean distance between two plain points.
    input: coordinates of the points
    output: Euclidean distance between the points.
"""


def distance(x1, y1, x2, y2):
    if x1 is None or x2 is None or y1 is None or y2 is None:
        return None
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def test_distance():
    assert (distance(None, 2, 3, 4) is None)
    assert (distance(2, None, 3, 4) is None)
    assert (distance(2, 3, None, 4) is None)
    assert (distance(None, 2, 3, None) is None)
    assert (distance(1, 5, 4, 1) == 5)
    assert (distance(0, 0, 1, 1) == math.sqrt(2))
    assert (distance(0, 0, -1, -1) == math.sqrt(2))


test_distance()
