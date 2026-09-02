# به نام خدا
import streamlit as st
from monty_hall import play_game, simulation_game

st.image("src/images/monty_hall.webp")


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
st.title(" :zap: Monty Hall Simulation")

num_games = st.number_input(
    "تعداد بازی‌هایی که می‌خواهید شبیه‌سازی کنید را وارد کنید",
    min_value=1,
    max_value=10000,
    value=100,
)

left_col, right_col = st.columns(2)

left_col.subheader("درصد برد بدون تغییر")
left_col.metric("درصد نهایی", f"{simulation_game(num_games, 'stay'):.1f}")
left_col.line_chart(running_win_rate("stay", num_games))

right_col.subheader("درصد برد با تغییر")
right_col.metric("درصد نهایی", f"{simulation_game(num_games, 'switch'):.1f}")
right_col.line_chart(running_win_rate("switch", num_games))
