# به نام خدا

'''
Writing a function to raise one number to another power
'''

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)
exponent(2, 5)
