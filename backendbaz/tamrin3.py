# به نام خدا

'''
Age & Income Loan Condition
'''


age = int(input("Enter your age: "))
income = float(input("Enter your income (in Tomans): "))

if age > 18:
    if income > 5_000_000:
        print("شما واجد شرایط وام هستید")
    else:
        print("شما واجد شرایط وام نیستید")

else:
    print("سن شما برای وام مناسب نیست")