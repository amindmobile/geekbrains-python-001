# main for de/serialize
# Можно увлечься и обвесить код улучшайзерами, проверяльщиками и крутизной. В основную задачу это не входило.
# импорт функций сохранения словаря в файл (pickle и json форматы)
from music_serialize import pickle_save, json_save
# импорт функций чтения словаря из файла (pickle и json форматы)
from music_deserialize import pickle_read, json_read

my_favourite_group = dict(name="Машина времени",  # сконструирован словарь
						  tracks=["Марионетки", "Разговор в поезде", "Костёр", "Синяя птица"],
						  Albums=[{"name": "Медленная хорошая музыка", "year": 1991},
								  {"name": "Картонные крылья любви", "year": 1996}])

if __name__ == '__main__':
	# сериализовать словарь my_favourite_group в файл pickle
	pickle_save(my_favourite_group)
	# сериализовать словарь my_favourite_group в файл json
	json_save(my_favourite_group)
	# десериализовать и вывести на экран словарь pickle из файла group.pickle
	print(pickle_read('group.pickle'))
	# десериализовать и вывести на экран сформированный функцией json_read словарь из файла group.json
	print(json_read('group.json'))
