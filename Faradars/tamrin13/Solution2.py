# به نام خدا

'''
Print half pyramid pattern facing down
Solution 2
'''

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print()
