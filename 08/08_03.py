# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента будет принимать атакующего и
# атакуемого. В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони
# персонажа). Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле
# damage / armor. Следовательно, у вас должно быть 2 функции: Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне. Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления
# урона и вычитания его из здоровья персонажа.

player_name = input("Введите имя игрока: ")
player = {"name": player_name, "health": 80, "damage": 45, "armor": 2.5}
enemy = {"name": "'Phycodurus eques'", "health": 100, "damage": 60, "armor": 1.2}


def pure_damage(damage, armor):
	return damage / armor


def attack(pers1, pers2):
	damage = pure_damage(pers1["damage"], pers2["armor"])
	pers2["health"] -= damage
	print(pers1["name"], "атакует", pers2["name"], "for", damage, "HP")
	print(pers2["name"], "здоровье:", pers2["health"], "HP")
	print(pers1["name"], "здоровье:", pers1["health"], "HP")


attack(player, enemy)
attack(enemy, player)
# print(player, enemy)
