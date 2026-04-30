# به نام خدا

'''
Student Discount Eligibility
'''


while True:
    try:
        age = int(input("Enter your age: "))
        break
    except:
        print("Invalid input")

while True:
    try:
        student = int(input("are you student? (1=Yes , 0=No): "))
        if student == 0 or student == 1:
            break
        else:
            print("Only 0 or 1 allowed")
    except:
        print("Invalid input")

if 18 <= age <= 25 and student == 1:
    print("شما می‌توانید از تخفیف استفاده کنید")
else:
    print("تخفیف شامل حال شما نمی‌شود")
