import json
from os import name, truncate
import os.path
from time import time


path_files = "src/files"
path_arch = os.path.join(os.getcwd(), path_files)
archivo = "ratings.json"


def save_score(user, level, score):
    """ Funcion que recibe un puntaje de un usuario y lo almacena en el nivel correspondiente """

    with open(os.path.join(path_arch, archivo), "r") as file:
        data = json.load(file)
        stringLevel = str(f"{level[0]}x{level[1]}")
        scores = data[stringLevel]
        scores.append((user, score))
        data[stringLevel] = sorted(scores, key = lambda score: score[1], reverse = True)


    with open(os.path.join(path_arch, archivo), "w") as file:
        json.dump(data, file, indent = 4)


def get_scores():
    """ Funcion que devuelve todos los datos de los puntajes """

    with open(os.path.join(path_arch, archivo), "r") as file:
        data = json.load(file)

    return data