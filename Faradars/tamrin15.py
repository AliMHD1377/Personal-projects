# به نام خدا

'''
Generate 3 random integers divisible by 5 between 100 and 999
'''

import random


print("Generating 3 random integer number between 100 and 999 divisible by 5:")
for num in range(3):
    print(random.randrange(100, 999, 5), end=', ')
