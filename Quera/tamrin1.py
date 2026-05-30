# به نام خدا

"""
Find the b-th prime number after n, where b is the sum of digits of n.
Author: AliMhd
"""


# Check if a number is prime
def is_prime(num):
    """Return True if num is prime, otherwise False."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
b = sum(int(d) for d in str(n))

# Find b-th prime number after n
count = 0
candidate = n + 1
while count < b:
    if is_prime(candidate):
        count += 1
    candidate += 1

print(candidate - 1)
