# به نام خدا

'''
Calculating the sum and multiplication of 2 numbers
'''

def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 100
    if product <= 100:
        return product
    else:
        # product is greater than 100 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)
