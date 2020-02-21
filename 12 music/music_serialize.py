#  music_serialize
import pickle
import json


# указать имя файла для экспорта (по умолчанию 'group'
def pickle_save(pickle_to_save, filename='group'):
	# открыть байт-файл на запись, в формате и с расширением .pickle
	with open(filename + ".pickle", 'wb') as file:
		# сохранить информацию в файл
		pickle.dump(pickle_to_save, file)
		# уведомить консоль об успехе
		print(f"Сериализован файл: '{file.name}'")


# указать имя файла для экспорта (по умолчанию 'group'
def json_save(json_to_save, filename='group'):
	# открыть файл на запись, в формате и с расширением .json, в кодировке UTF8
	with open(filename + ".json", 'w', encoding='UTF8') as file:
		# сохранить информацию в файл
		json.dump(json_to_save, file)
		# уведомить консоль об успехе
		print(f"Сериализован файл: '{file.name}' with {file.encoding} encoding.")
