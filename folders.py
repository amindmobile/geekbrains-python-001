#  Пока неясно как быть в сообщениях с разницей понятий folder/directory. Вероятно, в боевом коде делается проверка на
#  платформу.
import os
# import sys

# platform = sys.platform  # Определяем текущую платформу (windows, macos и т.п.)


def create_dirs(start, end):
	for i in range(start, end):  # срабатывания цикла также используется для именования создаваемых директорий
		folders_path = os.path.join(os.getcwd(), '{}_{}'.format("dir", i))
		if os.path.exists(folders_path):  # не создавать уже существующие директории
			print(f"Not created: '{folders_path}', already exists.")  # Сообщаем почему не создана папка
		else:
			os.mkdir(folders_path)  # создать директорию (каталог) используя "folders_path", где объединяются в путь:(
		# локальный каталог + название платформы (win32, macos и т.п.) + (номер (имя) директории из цикла от 1 до 10)
			print(f"Создано: '{folders_path}'")


def remove_dirs(start, end):
	if start and end:
		for i in range(start, end):
			folders_path = os.path.join(os.getcwd(), '{}_{}'.format("dir", i))
			if os.path.exists(folders_path):
				os.rmdir(folders_path)  # функция идентична создающей директории. Изменена только команда mkdir на rmdir
				print(f"Удалено: '{folders_path}'")  # сообщаем об успехе
			else:
				print(f"Директория для удаления не существует: {folders_path}")  # Сообщаем почему не удалено
	else:
		print("Не указаны директории для удаления")


if __name__ == '__main__':
	create_dirs()
	remove_dirs()
