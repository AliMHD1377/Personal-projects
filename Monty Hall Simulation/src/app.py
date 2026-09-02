# به نام خدا
import random
import streamlit as st


st.image("src/images/monty_hall.webp")


def play_game(strategy):
    initial_choice = random.choice(range(3))

    doors = ["car", "goat", "goat"]
    random.shuffle(doors)

    for i in range(3):
        if i != initial_choice and doors[i] == "goat":
            monty_opens = i
            break

    if strategy == "switch":
        for i in range(3):
            if i != initial_choice and i != monty_opens:
                final_choice = i
    else:
        final_choice = initial_choice

    return doors[final_choice] == "car"


# درصد بردِ لحظه‌به‌لحظه (برای نمودار خطی)
def running_win_rate(strategy, num_games):
    wins = 0
    rates = []
    for i in range(1, num_games + 1):
        if play_game(strategy):
            wins += 1
        rates.append(wins / i)
    return rates


# ---------- رابط کاربری ----------
st.title("Monty Hall Simulation")

num_games = st.number_input(
    "تعداد بازی‌هایی که می‌خواهید شبیه‌سازی کنید را وارد کنید",
    min_value=1,
    max_value=10000,
    value=100,
)

stay_rates = running_win_rate("stay", num_games)
switch_rates = running_win_rate("switch", num_games)

left_col, right_col = st.columns(2)

left_col.subheader("درصد برد بدون تغییر")
left_col.line_chart(stay_rates)

right_col.subheader("درصد برد با تغییر")
right_col.line_chart(switch_rates)
