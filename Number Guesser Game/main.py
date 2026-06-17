# به نام خدا

'''
بازی حدس عدد
'''

import random


score = 100
random_number = random.randint(1, 100)

game_over = False
while not game_over:
    while True:
        try:
            n = input("guess a number: ")
            if n == 'q':
                game_over = True
                break
            n = int(n)
            break
        except:
            print("guess a valid number please: ")

    if game_over == True:
        print("خداحافظ")
        break

    if n == random_number:
        print("حدس شما درست بود")
        print("score:", score)
        break

    elif n > random_number:
        print("عدد کمتری را حدس بزنید")
        score -= 1

    else:
        print("عدد بزرگتری را حدس بزنید")
        score -= 1
