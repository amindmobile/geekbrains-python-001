#  music_deserialize
import pickle
import json


# указать имя файла для чтения (по умолчанию 'group.pickle'
def pickle_read(pickle_to_read='group.pickle'):
	# открыть байт-файл на чтение
	with open(pickle_to_read, 'rb') as file:
		# вернуть информацию из файла в виде словаря
		return dict(pickle.load(file))


# указать имя файла для чтения (по умолчанию 'group.json'
def json_read(json_to_read='group.json'):
	# открыть файл на чтение в кодировке UTF-8
	with open(json_to_read, 'r', encoding='UTF8') as file:
		# вернуть информацию из файла в виде словаря
		return dict(json.load(file))
