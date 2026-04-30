# به نام خدا

'''
Remove the first n characters of a string
'''

def remove_chars(str, n):
    if n < 0 or n > len(str):
        raise ValueError("The value of n must be less than the length of the string and non-negative.")
    return str[n:]

print(remove_chars('orange', 4))
print(remove_chars('Iran', 1))
