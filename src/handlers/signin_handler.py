import json
import os.path


path_files = "src/files"
path_arch = os.path.join(os.getcwd(), path_files)
arch = "users.json"


def load_user(user, gender, age):
    """ Funcion que recibe un usuario y lo carga en la base de datos """

    enable = False
    
    with open(os.path.join(path_arch, arch), "r") as file:
        users_data = json.load(file)

    if not user in users_data:
        enable = True
        if users_data is not None:
            users_data[user] = {'Gender': gender, 'Age': age, 'Level': '6x4', 'Time': '2', 'Match': '2', 'Elem': 'Imagenes', 'Help': 'No', 'Theme': 'Noche', 'TxtWin': 'Felicitaciones, ganaste', 'TxtLose': 'Perdiste, volve a intentar', 'TxtTime': 'Cuidado, te queda poco tiempo'}
        else:
            users_data = {user: {'Genero': gender, 'Age': age, 'Level': '6x4', 'Time': '2', 'Match': '2', 'Elem': 'Imagenes', 'Help': 'No', 'Theme': 'Noche', 'TxtWin': 'Felicitaciones, ganaste', 'TxtLose': 'Perdiste, volve a intentar', 'TxtTime': 'Cuidado, te queda poco tiempo'}}

    with open(os.path.join(path_arch, arch), "w") as file:
        json.dump(users_data, file, indent = 4)

    return enable
    