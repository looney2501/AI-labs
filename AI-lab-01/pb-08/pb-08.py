from queue import Queue

"""
    Generate all binary numbers lower than a given number n
    input: number n, n > 0
    output: list of strings representing binary numbers, or None if n < 1
"""


def generate_binary_numbers_lower_than(n):
    if n is None or n < 1:
        return None
    q = Queue()
    q.put("1")
    result = []
    while n > 0:
        current_binary = q.get()
        result.append(current_binary)
        q.put(current_binary + '0')
        q.put(current_binary + '1')
        n -= 1
    return result


def test_generate_binary_numbers_lower_than():
    assert (generate_binary_numbers_lower_than(None) is None)
    assert (generate_binary_numbers_lower_than(0) is None)
    assert (generate_binary_numbers_lower_than(1) == ['1'])
    assert (generate_binary_numbers_lower_than(4) == ['1', '10', '11', '100'])


test_generate_binary_numbers_lower_than()
