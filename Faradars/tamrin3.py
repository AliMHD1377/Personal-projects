# به نام خدا

'''
Print characters in a string with even index numbers
'''

s = input("Enter a str:")

print(f'Original String: {s}')
print('Printing only even index chars')

size = len(s)

# step: 2 to get the characters present at even index like 0, 2, 4
for i in range(0, size - 1, 2):
    print(f'index[ {i} ] {s[i]}')
