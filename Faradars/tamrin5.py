# به نام خدا

'''
Checking if the first and last element of a list are the same
'''

def first_last_same(num):
    print(f'Given list: {num}')
    if num[0] == num[-1]:
        return True
    else:
        return False

L1 = [10, 20, 30, 40, 10]
print('result is', first_last_same(L1))

L2 = [75, 65, 35, 75, 30]
print('result is', first_last_same(L2))
