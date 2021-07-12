import json
import os.path


path_files = "src/files"
path_arch = os.path.join(os.getcwd(), path_files)
archivo = "users.json"

#=======================FUNCIONES QUE GUARDAN DATOS=======================

def general(name, v):
	""" Funcion que guarda la configuracion general """

	with open(os.path.join(path_arch, archivo), "r") as file:
		data = json.load(file)
		data[name]['Level'] = v['-Level-']
		data[name]['Time'] = v['-Time-']
		data[name]['Match'] = v['-Match-']
		data[name]['Elem'] = v['-Elem-']
		data[name]['Help'] = v["-Help-"]
		data[name]['Theme'] = v['-Theme-']

	with open(os.path.join(path_arch, archivo), "w") as file:
		json.dump(data, file, indent=4)

def txtwin(name, t):
	""" Funcion que guarda la configuracion de texto a mostrar cuando se gana """

	with open(os.path.join(path_arch, archivo), "r") as file:
		data = json.load(file)
		data[name]['TxtWin'] = t['-TxtWin-']

	with open(os.path.join(path_arch, archivo), "w") as file:
		json.dump(data, file, indent=4)

def txtlos(name, t):
	""" Funcion que guarda la configuracion de texto a mostrar cuando se pierde"""

	with open(os.path.join(path_arch, archivo), "r") as file:
		data = json.load(file)
		data[name]['TxtLose'] = t['-TxtLose-']

	with open(os.path.join(path_arch, archivo), "w") as file:
		json.dump(data, file, indent=4)

def txttime(name, t):
	""" Funcion que guarda la configuracion de texto a mostrar cuando queda poco tiempo"""

	with open(os.path.join(path_arch, archivo), "r") as file:
		data = json.load(file)
		data[name]['TxtTime'] = t['-TxtTime-']

	with open(os.path.join(path_arch, archivo), "w") as file:
		json.dump(data, file, indent=4)


#=======================FUNCIONES QUE RETORNAN DATOS=======================

def get_level(name):
	""" Funcion que retorna la configuracion de la dificultad de un usuario """

	with open(os.path.join(path_arch, archivo), "r") as file:
		data = json.load(file)
		level = data[name]['Level']

	level = list(level.replace('x',''))
	level = list(map(lambda num: int(num), level))

	try:
		level[1] = (level[1] * 10) + level[2]
	except IndexError:
		pass

	return level


def get_time(name):
	""" Funcion que retorna la configuracion del tiempo de un usuario """

	with open(os.path.join(path_arch, archivo), "r") as file:
		data = json.load(file)
		time = data[name]['Time']

	return int(time)


def get_elem(name):
	""" Funcion que retorna la configuracion de los elementos de un usuario """

	with open(os.path.join(path_arch, archivo), "r") as file:
		data = json.load(file)
		elem = data[name]['Elem']

	return elem


def get_theme(name):
	""" Funcion que retorna la configuracion del tema de un usuario """

	with open(os.path.join(path_arch, archivo), "r") as file:
		data = json.load(file)
		theme = data[name]['Theme']

	if (theme == 'Noche'):
		theme = 'Darkpurple1'
	elif (theme == 'Dia'):
		theme = 'Reddit'
	else:
		theme = 'LightGreen3'

	return theme

def get_setting(name):
	""" Funcion que retorna la configuracion completa de un usuario """

	with open(os.path.join(path_arch, archivo), "r") as file:
		data = json.load(file)
		setting = data[name]

	return setting
