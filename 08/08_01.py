# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку
# вида «Василий, 21 год(а), проживает в городе Москва»


def task1(name, age, city):
	return f'{name}, {age} год(а), проживает в городе {city}.'


print(task1("Xian", 23, "Гуанчжоу"))
print(task1("Celeste", 34, "Paris"))


# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def task2(num1, num2, num3):
	nums = [num1, num2, num3]
	return f'Из предложенных цифр: {num1}, {num2}, {num3} наибольшей является: {max(nums)}'


print(task2(3, 5, 7))


def task2a(num1, num2, num3):
	return max([num1, num2, num3])


print(task2a(3, 5, 7))

