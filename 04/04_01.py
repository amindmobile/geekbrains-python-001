# Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.

# это мой пример
list_1 = [2, 5, 8, 2, 12, 12, 4]
list_2 = [2, 7, 12, 3]
list_1_new = []
for num in list_1:
	if num not in list_2:
		list_1_new.append(num)
print(list_1_new)

# это "правильный" пример предложенный в видео
list_1 = [2, 5, 8, 2, 12, 12, 4]
list_2 = [2, 7, 12, 3]
for number in list_1:
	if number in list_2[:]:
		list_1.remove(number)
print(list_1)
