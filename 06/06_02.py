# Практика. Игра "угадай число" промежуточная версия (по видео)
import random

number = random.randint(1, 100)
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input("Выбери уровень сложности: "))
max_count = levels[level]

while user_number != number:
	count += 1
	if count > max_count:
		print("Вы проиграли!")
		break
	print(f"Попытка № {count}")
	user_number = int(input("Введите число от 1 до 100: "))
	if user_number < number:
		print("Загаданное число больше")
	elif user_number > number:
		print("Загаданное число меньше")
	else:
		print("Вы пока не угадали")
else:
	print("Вы угадали!")
