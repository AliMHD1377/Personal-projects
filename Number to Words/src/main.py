from constants import ABOVE_100, TENS, UNDER_20


def num_to_word(num: int) -> str:
    """
    Function converts an integer into words.

    :param int num: عددی که باید به حروف تبدیل شود
    :return: نمایش نوشتاری عدد
    :rtype: str
    """
    # If the number is less than 20, use direct mapping.
    if num < 20:
        return UNDER_20[num]

    # If the number is less than 100, calculate tens and ones separately.
    if num < 100:
        return TENS[num // 10 - 2] + ("" if num % 10 == 0 else " " + UNDER_20[num % 10])

    # For numbers 100 and above, calculate words recursively.
    pivot = max([key for key in ABOVE_100 if key <= num])

    p1 = num_to_word(num // pivot)
    p2 = ABOVE_100[pivot]
    if num % pivot == 0:
        return f'{p1} {p2}'

    return f'{p1} {p2} {num_to_word(num % pivot)}'


if __name__ == "__main__":
    while True:
        user_input = input("Enter a Number (q to quit): ").strip()
        if user_input.lower() == 'q':
            break
        try:
            num = int(user_input)
        except ValueError:
            print("ورودی نامعتبر! دوباره تلاش کنید.\n")
            continue

        if 0 <= num <= 999_999_999_999:
            print(f"پاسخ: {num_to_word(num)}\n")
        else:
            print("Number out of range (must be 0 to 999,999,999,999)\n")
