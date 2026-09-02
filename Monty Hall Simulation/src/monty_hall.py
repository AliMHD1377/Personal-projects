# به نام خدا

import random

def play_game(strategy):

    initial_choice = random.choice(range(3))

    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    # دری که قراره مانتی آشکار کند
    for i in range(3):
        if i != initial_choice and doors[i] == 'goat':
            monty_opens = i
            break

    if strategy == "switch":
        for i in range(3):
            if i != initial_choice and i != monty_opens:
                final_choice = i
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'

def simulation_game(num_games , strategy):
    wins = 0
    for _ in range(num_games):
        if play_game(strategy):
            wins += 1
    return wins / num_games * 100

if __name__ == "__main__":
    num_games = 100000
    switch_win = simulation_game(num_games, "switch")
    stay_win = simulation_game(num_games, "stay")
    print(f"Win percentage with switch: {switch_win}")
    print(f"Win percentage with stay: {stay_win}")
