from os import chdir, listdir, path, rmdir, remove, mkdir, getcwd, pardir
from shutil import copy, copytree
from datetime import datetime


def create_file(name, text=None):  # Создание файла
	with open(name, 'w', encoding='utf-8') as file:
		if text:
			file.write(text)
			print(f"Created file: {name}")


def create_folder(name):  # Создание папки/каталога
	try:
		mkdir(name)
	except FileExistsError:
		print('Такая папка уже существует')


def get_list(folders_only=False):  # Получить список файлов в текущем местоположении
	result = listdir()
	if folders_only:
		result = [file for file in result if path.isdir(file)]
	print(result)


def delete_file(name):  # Удаление файла
	if path.isdir(name):
		rmdir(name)
		print(f"Deleted file {name}")
	else:
		remove(name)
		print(f"Deleted file {name}")


def copy_file(old_name, new_name):  # Копирование файла
	if path.isdir(old_name):
		try:
			copytree(old_name, new_name)
			print(f"Copied {old_name} to {new_name}")
		except FileExistsError:
			print('Такая папка уже существует')
	else:
		copy(old_name, new_name)
		print(f"Copied {old_name} to {new_name}")


def save_info(message):  # Сохранить лог
	current_time = datetime.now()
	result = f'{current_time} - {message}'
	with open('log.txt', 'a', encoding='utf-8') as log_file:
		log_file.write(result + '\n')


def helpme():  # Получить помощь
	help_list = ['list - список файлов и папок',
				 'create_file - создание файла',
				 'create_folder - создание папки',
				 'delete - удаление файла или папки',
				 'copy - копирование файла или папки',
				 'ch - перейти в каталог',
				 'up - перейти на уровань выше']

	for i in help_list:
		print(i)


def ch(dir_path):  # Изменить текущее местоположение. Для нормальной работы должен быть наверное цикл.
	# Но это не является сутью задания.
	try:
		chdir(dir_path)
		print(getcwd())
	except WindowsError:
		print("Задан неверный путь")
	except OSError:
		print("Проблема в заданном пути")


def up():  # Переместиться уровнем выше относительно текущего местоположения
	chdir(pardir)


if __name__ == '__main__':
	print(getcwd())
