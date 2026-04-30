# به نام خدا

'''
Writing a program to extract each digit of an integer in reverse order
'''

number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10

    print(digit, end=" ")
    number = number // 10
