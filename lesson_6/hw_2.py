user_num = input("Введіть число від 0 до 8640000: ").strip()

if not user_num.isdigit():
    print("Помилка: потрібно ввести ціле невідʼємне число.")
    exit()

total_seconds = int(user_num)

if total_seconds < 0 or total_seconds > 8640000:
    print("Помилка: необхідно ввести число від 0 до 8640000.")
    exit()

sec_day = 86400
sec_hour = 3600
sec_min = 60

days, remainder = divmod(total_seconds, sec_day)
hours, remainder = divmod(remainder, sec_hour)
minutes, seconds = divmod(remainder, sec_min)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not 12 <= days % 100 <= 14:
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {hours:02}:{minutes:02}:{seconds:02}")