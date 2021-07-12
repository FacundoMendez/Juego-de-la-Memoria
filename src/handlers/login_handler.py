import json
import os.path


path_files = "src/files"
path_arch = os.path.join(os.getcwd(), path_files)
arch = "users.json"


def check_user(user):
    """ Funcion que recibe un usuario y verifica si existe para poder iniciar sesion """
    
    enable = False

    with open(os.path.join(path_arch, arch), "r") as file:
        users_data = json.load(file)

    if user in users_data:
        enable = True

    return enable