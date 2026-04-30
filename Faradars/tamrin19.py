# به نام خدا

'''
Rolling a die with the specified condition
'''

import random


dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
for i in range(5):
    random.seed(80)
    print(random.choice(dice))
