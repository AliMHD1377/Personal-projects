# به نام خدا

'''
Displaying numbers divisible by 5 in a list
'''

num_list = [10, 20, 33, 46, 55]

print('Given list:', num_list)
print('Divisible by 5:')
for i in num_list:
    if i % 5 == 0:
        print(i)
