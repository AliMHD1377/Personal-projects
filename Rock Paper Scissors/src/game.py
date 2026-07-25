import random


class RockPaperScissors():
    def __init__(self):
        self.choices = ['Rock', 'Paper', 'Scissors']
    
    def get_user_choice(self):
        while True:
            user_choice = input(f'Enter your choice: {self.choices}: ')
            if user_choice in self.choices:
                return user_choice
            print(f"invalid choice. you must select from {self.choices}.")

    def get_computer_choice(self):
        computer_choice = random.choice(self.choices)
        return computer_choice

    def determine_winner(self, user_choice, computer_choice):
        win_combinations = [('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')]

        if user_choice == computer_choice:
            print('مساوی')
        elif (user_choice, computer_choice) in win_combinations:
            print('شما بردید')
        else:
            print('کامپیوتر برد')

    def play(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"Computer choice: {computer_choice}")
        self.determine_winner(user_choice, computer_choice)
            

if __name__ == '__main__':
    game = RockPaperScissors()

    while True:
        game.play()
        again = input('do you wana play again? y or n: ')
        if again == 'y':
            continue
        else:
            break
