# به نام خدا

'''
Sum of numbers from 1 to user's number
'''


num = int(input("Enter a number: "))

total = 0
for i in range(1, num + 1):
    total += i

print(f"Sum of numbers from 1 to {num} is: {total}")
