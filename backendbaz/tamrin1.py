# به نام خدا

'''
Valid number input
'''


while True:
    try:
        num = float(input("Enter a number: "))
        break
    except:
        print("Invalid input! Please enter a valid number.")
