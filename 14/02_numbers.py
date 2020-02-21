# Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих след/условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.

nums = [num for num in range(-10, 11)]
multi = [num for num in nums if num % 3 == 0]
positive = [num for num in nums if num > 0]
not_multi = [num for num in nums if num % 4 != 0]

print(f"Обрабатываемый список чисел: {nums}")
print(f"Кратны числу 3: {multi}")
print(f"Положительные: {positive}")
print(f"Не кратны числу 4: {not_multi}")
