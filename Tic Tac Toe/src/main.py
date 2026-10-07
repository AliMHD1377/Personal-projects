# به نام خدا

import random


class TicTacToe:
    def __init__(self):
        # صفحه بازی به صورت لیست دو بعدی با اعداد 1 تا 9
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        # مجموعه خانه‌های معتبر باقی‌مانده
        self.valid_cells = {str(i) for i in range(1, 10)}
        # انتخاب تصادفی بازیکن شروع‌کننده
        self.current_player = random.choice(['X', 'O'])

    def __str__(self):
        """نمایش رشته‌ای صفحه بازی"""
        rows = []
        for row in self.board:
            rows.append(' | '.join(row))
        return '\n---------\n'.join(rows)

    def print_board(self):
        """چاپ وضعیت فعلی صفحه"""
        print('\n' + str(self) + '\n')

    def play(self):
        """اجرای یک حرکت توسط بازیکن جاری"""
        while True:
            self.print_board()
            print(f"نوبت بازیکن: {self.current_player}")
            move = input("Choose an empty square: ").strip()

            if move not in self.valid_cells:
                print("ورودی نامعتبر! لطفاً یک عدد از خانه‌های خالی وارد کنید.\n")
                continue

            # پیدا کردن موقعیت خانه در صفحه
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == move:
                        self.board[i][j] = self.current_player

            self.valid_cells.remove(move)
            break

    def check_winner(self):
        """بررسی برنده شدن بازیکن جاری"""
        b = self.board
        # بررسی سطرها
        for row in b:
            if row[0] == row[1] == row[2]:
                return row[0]
        # بررسی ستون‌ها
        for col in range(3):
            if b[0][col] == b[1][col] == b[2][col]:
                return b[0][col]
        # بررسی قطرها
        if b[0][0] == b[1][1] == b[2][2]:
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0]:
            return b[0][2]
        return None

    def switch_player(self):
        """تغییر نوبت بازیکن"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_full(self):
        """بررسی پر شدن صفحه"""
        return len(self.valid_cells) == 0


def start():
    game = TicTacToe()
    print("به بازی دوز خوش آمدید!")

    while True:
        game.play()
        winner = game.check_winner()

        if winner:
            game.print_board()
            print(f"player {winner} won!🎉")
            break

        if game.is_full():
            game.print_board()
            print("بازی مساوی شد! 🤝")
            break

        game.switch_player()


if __name__ == "__main__":
    start()