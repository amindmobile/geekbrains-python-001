# Практика. Игра "угадай число" финальная версия
import random

number = random.randint(1, 100)
print(number)
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input("Выбери уровень сложности: "))
max_count = levels[level]
user_count = int(input("Введите количество игроков: "))
users = []
for i in range(user_count):
	user_name = input(f"Введите имя игрока {i} ")
	users.append(user_name)
print(users)

is_winner = False
winner_name = None

while not is_winner:
	count += 1
	if count > max_count:
		print("Все игроки проиграли!")
		break
	print(f"Попытка № {count}")
	for user in users:
		print(f"Ход пользователя {user}")
		# Шаг 2: Предложить игроку ввести число
		user_number = int(input("Введите число от 1 до 100: "))
		if user_number == number:
			is_winner = True
			winner_name = user
			break
		# Шаг 3: Сравниваем числа и выводим результат
		if user_number < number:
			print("Загаданное число больше")
		elif user_number > number:
			print("Загаданное число меньше")
		else:
			print("Вы пока не угадали")
else:
	print(f"Победитель {winner_name}")
