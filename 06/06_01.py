# Практика. Игра "угадай число" начальная версия (по видео)
import random


number = random.randint(1, 100)
# print(number)

while True:
	user_number = int(input("Введите число от 1 до 100: "))
	if user_number == number:
		print("Вы угадали!")
		break
	elif user_number < number:
		print("Загаданное число больше")
	elif user_number > number:
		print("Загаданное число меньше")
