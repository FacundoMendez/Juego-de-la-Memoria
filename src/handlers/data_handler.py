import csv
from random import shuffle
from itertools import repeat
import datetime
import os.path
from src.handlers import settings_handler


# -----------------------------Primera base de datos-----------------------------

def make_reader_countries():
    ''' Funcion simple para abrir el archivo y retornarlo para recorrer '''

    path_files = "src/files"
    path_arch = os.path.join(os.getcwd(), path_files)
    archivo = "countries_of_the_world.csv"
    
    file = open(os.path.join(path_arch, archivo), 'r', encoding = 'utf-8')
    countries = csv.reader(file, delimiter = ',')
    next(countries)

    return countries


# ---------- Funciones que devuelven datos filtrados ----------

def get_biggest_population(elements, user, match):
    ''' Funcion que retorna los paises con mayor poblacion '''
    
    countries = make_reader_countries()

    countries = sorted(countries, key = lambda country: int(country[2]), reverse = True)
    data = [(countries[index][0],f'{countries[index][0].replace(" ","")}.png') for index in range(0,int(elements/match))]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda country: country[0], data))
    else:
        data = list(map(lambda country: country[1], data))

    data = [x for item in data for x in repeat(item, 2)]

    shuffle(data)

    return data


def get_europe_america(elements, user, match):
    ''' Funcion que retorna los paises de europa y america '''
    
    countries = make_reader_countries()

    aux_countries = list(map(lambda country: (country[0], country[1].replace(' ', '')), countries))
    america_and_europe = [country[0] for country in aux_countries if (country[1] == 'LATINAMER.&CARIB' or country[1] == 'WESTERNEUROPE')]
    data = [(america_and_europe[index],f'{america_and_europe[index].replace(" ","")}.png') for index in range(0,int(elements/match))]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda country: country[0], data))
    else:
        data = list(map(lambda country: country[1], data))

    data = [x for item in data for x in repeat(item, 2)]

    shuffle(data)

    return data


def get_africa_asia_oceania(elements, user, match):
    ''' Funcion que retorna los paises de africa, asia y oceania '''

    countries = make_reader_countries()

    aux_countries = list(map(lambda country: (country[0], country[1].replace(' ', '')), countries))
    africa_asia_oceania = [country[0] for country in aux_countries if not(country[1] == 'LATINAMER.&CARIB' or country[1] == 'WESTERNEUROPE')]
    data = [(africa_asia_oceania[index],f'{africa_asia_oceania[index].replace(" ","")}.png') for index in range(0,int(elements/match))]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda country: country[0], data))
    else:
        data = list(map(lambda country: country[1], data))

    data = [x for item in data for x in repeat(item, 2)]

    shuffle(data)

    return data


def get_biggest_surface(elements, user, match):
    ''' Funcion que retorna los paises con mayor superficie '''

    countries = make_reader_countries()

    countries = sorted(countries, key = lambda country: int(country[3]), reverse = True)
    data = [(countries[index][0],f'{countries[index][0].replace(" ","")}.png') for index in range(0,int(elements/match))]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda country: country[0], data))
    else:
        data = list(map(lambda country: country[1], data))

    data = [x for item in data for x in repeat(item, 2)]

    shuffle(data)

    return data


def get_lowest_population(elements, user, match):
    ''' Funcion que retorna los paises con menor poblacion '''

    countries = make_reader_countries()

    countries = sorted(countries, key = lambda country: int(country[2]))
    data = [(countries[index][0],f'{countries[index][0].replace(" ","")}.png') for index in range(0,int(elements/match))]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda country: country[0], data))
    else:
        data = list(map(lambda country: country[1], data))

    data = [x for item in data for x in repeat(item, 2)]

    shuffle(data)

    return data


def get_highest_deathrate(elements, user, match):
    ''' Funcion que retorna los paises con mayor tasa de mortalidad '''
    
    countries = make_reader_countries()

    aux_countries = [(country[0], float(country[16].replace(',', '.'))) for country in countries if country[16] != '']
    highest_deathrate = sorted(aux_countries, key = lambda country: country[1], reverse = True)
    data = [(highest_deathrate[index][0],f'{highest_deathrate[index][0].replace(" ","")}.png') for index in range(0,int(elements/match))]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda country: country[0], data))
    else:
        data = list(map(lambda country: country[1], data))

    data = [x for item in data for x in repeat(item, 2)]

    shuffle(data)

    return data


def get_lowest_surface(elements, user, match):
    ''' Funcion que retorna los paises con menor superficie '''
    
    countries = make_reader_countries()

    countries = sorted(countries, key = lambda country: int(country[3]))
    data = [(countries[index][0],f'{countries[index][0].replace(" ","")}.png') for index in range(0,int(elements/match))]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda country: country[0], data))
    else:
        data = list(map(lambda country: country[1], data))

    data = [x for item in data for x in repeat(item, 2)]

    shuffle(data)

    return data

# -----------------------------Segunda base de datos-----------------------------

def make_reader_animals():
    ''' Funcion simple para abrir el archivo y retornarlo para recorrer '''

    path_files = "src/files"
    path_arch = os.path.join(os.getcwd(), path_files)
    archivo = "animals_spanish.csv"

    file = open(os.path.join(path_arch, archivo), 'r', encoding='utf-8')
    animals = csv.reader(file, delimiter=',')
    next(animals)

    return animals

# ---------- Funciones que devuelven datos filtrados ----------

def get_animales_sin_pelo(elements, user, matchs):
    """Funcion que retona una lista de animales sin pelo"""

    csvreader=make_reader_animals()
    animals=[]

    for animal in csvreader:
        if "0" in animal[1]:
            animals.append(animal[0])

    shuffle(animals)
    elem = int(elements / matchs)

    data = [(animals[i], f'{animals[i]}.png') for i in range(0, elem)]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda ani: ani[0], data))
    else:
        data = list(map(lambda ani: ani[1], data))

    data = [x for item in data for x in repeat(item, matchs)]

    shuffle(data)

    return(data)


def get_animales_no_acuaticos(elements, user, matchs):
    """Funcion que retona una lista de animales no acuaticos"""

    csvreader = make_reader_animals()
    animals = []

    for animal in csvreader:
        if "0" in animal[6]:
            animals.append(animal[0])

    shuffle(animals)
    elem = int(elements / matchs)

    data = [(animals[i], f'{animals[i]}.png') for i in range(0, elem)]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda ani: ani[0], data))
    else:
        data = list(map(lambda ani: ani[1], data))

    data = [x for item in data for x in repeat(item, matchs)]

    shuffle(data)

    return (data)


def get_animales_con_columna(elements, user, matchs):
    """Funcion que retona una lista de animales con columna vertebral"""

    csvreader = make_reader_animals()
    animals = []

    for animal in csvreader:
        if "1" in animal[9]:
            animals.append(animal[0])

    shuffle(animals)
    elem = int(elements / matchs)

    data = [(animals[i], f'{animals[i]}.png') for i in range(0, elem)]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda ani: ani[0], data))
    else:
        data = list(map(lambda ani: ani[1], data))

    data = [x for item in data for x in repeat(item, matchs)]

    shuffle(data)

    return (data)


def get_animales_sin_dientes(elements, user, matchs):
    """Funcion que retona una lista de animales sin dientes"""

    csvreader = make_reader_animals()
    animals = []

    for animal in csvreader:
        if "0" in animal[8]:
            animals.append(animal[0])

    shuffle(animals)
    elem=int(elements/matchs)

    data = [(animals[i], f'{animals[i]}.png') for i in range(0, elem)]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda ani: ani[0], data))
    else:
        data = list(map(lambda ani: ani[1], data))

    data = [x for item in data for x in repeat(item, matchs)]

    shuffle(data)

    return (data)


def get_animales_no_plumiferos(elements, user, matchs):
    """Funcion que retona una lista de animales sin plumas"""

    csvreader = make_reader_animals()
    animals = []

    for animal in csvreader:
        if "0" in animal[2]:
            animals.append(animal[0])

    shuffle(animals)
    elem = int(elements / matchs)

    data = [(animals[i], f'{animals[i]}.png') for i in range(0, elem)]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda ani: ani[0], data))
    else:
        data = list(map(lambda ani: ani[1], data))

    data = [x for item in data for x in repeat(item, matchs)]

    shuffle(data)

    return (data)


def get_animales_no_voladores(elements, user, matchs):
    """Funcion que retona una lista de animales que no vuelan"""

    csvreader = make_reader_animals()
    animals = []

    for animal in csvreader:
        if "0" in animal[5]:
            animals.append(animal[0])

    shuffle(animals)
    elem = int(elements / matchs)

    data = [(animals[i], f'{animals[i]}.png') for i in range(0, elem)]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda ani: ani[0], data))
    else:
        data = list(map(lambda ani: ani[1], data))

    data = [x for item in data for x in repeat(item, matchs)]

    shuffle(data)

    return (data)


def get_animales_no_depredadores(elements, user, matchs):
    """Funcion que retona una lista de animales depredadores"""

    csvreader = make_reader_animals()
    animals = []

    for animal in csvreader:
        if "0" in animal[7]:
            animals.append(animal[0])

    shuffle(animals)
    elem = int(elements / matchs)

    data = [(animals[i], f'{animals[i]}.png') for i in range(0, elem)]

    if settings_handler.get_elem(user) == 'Palabras':
        data = list(map(lambda ani: ani[0], data))
    else:
        data = list(map(lambda ani: ani[1], data))

    data = [x for item in data for x in repeat(item, matchs)]

    shuffle(data)

    return (data)

# -----------------------------

days_week = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
morning, afternoon =  [(0, 12), (13, 23)]

week_organization = {
    'lunes': {morning: {'function': get_biggest_population}, afternoon: {'function': get_animales_sin_pelo}},
    'martes': {morning: {'function': get_europe_america}, afternoon: {'function': get_animales_no_acuaticos}},
    'miercoles': {morning: {'function': get_africa_asia_oceania}, afternoon: {'function': get_animales_con_columna}},
    'jueves': {morning: {'function': get_biggest_surface}, afternoon: {'function': get_animales_sin_dientes}},
    'viernes': {morning: {'function': get_lowest_population}, afternoon: {'function': get_animales_no_plumiferos}},
    'sabado': {morning: {'function': get_highest_deathrate}, afternoon: {'function': get_animales_no_voladores}},
    'domingo': {morning: {'function': get_lowest_surface}, afternoon: {'function': get_animales_no_depredadores}}
}


def get_data(user):
    ''' Funcion que retorna los datos ya listos para mostrarse '''

    day = days_week[datetime.datetime.today().weekday()]
    hour = datetime.datetime.now().hour
    time_zone = morning if hour in morning else afternoon

    level = settings_handler.get_level(user)
    elements = level[0] * level[1]

    matchs = (int(settings_handler.get_setting(user)['Match']))

    data = week_organization[day][time_zone]['function'](elements, user, matchs)

    return data