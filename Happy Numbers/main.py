# به نام خدا

def is_happy(num: int) -> bool:
    """
    Checks whether a given number is happy or not.

    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum
    of the squares of its digits in base-ten, and repeat the process
    until the number either equals 1 (where it will stay), or it loops
    endlessly in a cycle that does not include 1. Those numbers for
    which this process ends in 1 are happy numbers.
    :Example:

    >>> is_happy(19)
    True

    >>> is_happy(2)
    False
    """
    seen_numbers = set()
    while num !=1 and num not in seen_numbers:
        seen_numbers.add(num)
        num = sum(int(i) ** 2 for i in str(num))
    return num == 1


if __name__ == "__main__":
    assert is_happy(19), 'Test Case 1 Failed'
    assert not is_happy(2), 'Test Case 2 Failed'
    assert is_happy(44), 'Test Case 3 Failed'
    assert is_happy(86), 'Test Case 4 Failed'
    assert is_happy(139), 'Test Case 5 Failed'

    print('All test cases pass')
