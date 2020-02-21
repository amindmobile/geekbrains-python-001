# Практика. Игра "угадай число". Домашнее задание.
# В задании говорилось, что нужно взаимодействовать с программой с помощью знаков <>=.
# Но, Я - ленивая пятая точка, поэтому автоматизировал поск программой загаданного числа. Пусть сама "нажимает" <>=
# В текущей реализации поиск решения является хаотичным брутфорсом.
# Возможно буду использовать этот код для изучения оптимизации поиска. Например "метод деления на два".
# Защита от "дурака" и неправильного ввода не планируется, т.к. целью текущего обучения на является.
import random

# user_number = int(input("Введите число от 1 до 100: "))
user_number = int(input("Please, enter your number to guess (from 1 to 100): "))  # Запрос числа от пользователя
used_numbers = []  # Хранятся использованные числа, которые не подошли как ответ.
answer_try = int(random.randint(0, 100))

while answer_try != user_number:

	if answer_try > user_number:
		answer_try = int(random.randint(0, answer_try))
		print(f"Моё предположение {answer_try}")
		if answer_try not in used_numbers:
			used_numbers.append(answer_try)
			if answer_try == user_number:
				print(f"Использованы числа: {used_numbers}")
				print("Попыток угадать:", len(used_numbers))
				print(f"Число угадано: {answer_try}")
				break

	elif answer_try < user_number:
		answer_try = int(random.randint(answer_try, 100))
		print(f"Моё предположение {answer_try}")
		if answer_try not in used_numbers:
			used_numbers.append(answer_try)
			if answer_try == user_number:
				print(f"Использованы числа: {used_numbers}")
				print("Попыток угадать:", len(used_numbers))
				print(f"Число угадано: {answer_try}")
				break
	else:
		print("Что-то пошло не так")
		break
