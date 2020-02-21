from sys import argv
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, helpme, ch
from game import game1

save_info('Старт')

try:
	command = argv[1]
except IndexError:
	helpme()
else:
	if command == 'list':
		get_list()
	elif command == 'create_file':
		try:
			name = argv[2]
		except IndexError:
			print('Не указано имя файла для создания')
		else:
			create_file(name)
	elif command == 'create_folder':
		try:
			name = argv[2]
		except IndexError:
			print('Не указано имя папки для создания')
		else:
			create_folder(name)
	elif command == 'delete':
		try:
			name = argv[2]
		except IndexError:
			print('Не указано имя папки или файла для удаления')
		else:
			delete_file(name)
	elif command == 'copy':
		try:
			old_name = argv[2]
			new_name = argv[3]
		except IndexError:
			print("Укажите имя файла и его назначения (копии)")
		else:
			copy_file(old_name, new_name)
	elif command == 'help':
		helpme()
	elif command == 'ch':
		try:
			path = argv[2]
		except IndexError:
			print('Не указан путь')
		else:
			ch(path)
	elif command == 'game1':
		game1()

	save_info('Стоп')
