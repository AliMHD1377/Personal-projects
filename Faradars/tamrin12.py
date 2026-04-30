# به نام خدا

'''
Printing the multiplication table from 1 to 10
'''

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i * j:3d}', end="") # فرمت بندی عدد به 4 کاراکتر
    print()
