# 3. Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список из квадратных
# корней # чисел (если число положительное) и самих чисел (если число отрицательное) и возвращает результат (желательно
# применить генератор и тернарный оператор при необходимости). В результате работы функции исходный список не должен
# измениться.
# если число во входящем списке положительное превратить в новом списке его в квадратный корень.
# Если отрицательное - оставить как есть
from math import sqrt
# В задании сказано создать список -0+ руками, но...
nums = [num for num in range(-5, 6)]


def func1(in_nums):
	# для красоты можно округлить num в round, но в задании этого не было
	new_nums = [sqrt(num) if num > 0 else num for num in in_nums]
	return new_nums


print(f"Исходный список чисел: {nums}")
print(f"Список обработанный функцией: {func1(nums)}")
