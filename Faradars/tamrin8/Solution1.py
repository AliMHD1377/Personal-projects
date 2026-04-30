# به نام خدا

'''
Checking whether a number is symmetrical
Solution 1
'''

def palindrome(num):
    num = str(num)
    print(f'orignal number {num}')
    reverse_num = num[::-1]
    if num == reverse_num:
        print('Yes. given number is palindrome number')
    else:
        print('No. given number is not palindrome number')


palindrome(121)
palindrome(125)
