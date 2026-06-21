# به نام خدا

'''
بازی حدس عدد
'''

import random


def statr_game():
    score = 100
    random_number = random.randint(1, 100)

    game_over = False
    while not game_over:
        while True:
            try:
                user_guess = input("Enter your guess between 1 and 100: ")
                if user_guess == 'q':
                    game_over = True
                    break
                user_guess = int(user_guess)
                break
            except:
                print("لطفا ورودی صحیحی را وارد کنید")

        if game_over == True:
            print("خداحافظ")
            break

        if user_guess == random_number:
            print("حدس شما درست بود")
            print("your score:", score)
            wanna_play = input("می خوای دوباره بازی کنی؟ y/n: ")
            if wanna_play == 'y':
                random_number = random.randint(1, 100)
                score = 100
                continue
            else:
                print("خداحافظ")
                break
        elif user_guess > random_number:
            print("عدد کمتری را حدس بزنید")
            
        else:
            print("عدد بزرگتری را حدس بزنید")
        
        score -= 1

if __name__ == '__main__':
    statr_game()
