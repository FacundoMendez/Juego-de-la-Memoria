import PySimpleGUI as sg
from src.handlers import settings_handler

def build(name):
    """ Funcion que construye la ventana de configuracion """

    sg.theme(settings_handler.get_theme(name))

    layout = [
        [sg.Text('Elija tamaño del tablero: ', pad = ((10,0),(40,5)), size=(36, 1), font = ('Pixel Font7',15)),
        sg.InputCombo(('6x4', '6x8', '6x12') ,background_color="old lace",pad = ((80,0),(40,10)),size=(20, 1), key="-Level-", font = ('Pixel Font7',15),default_value=settings_handler.get_setting(name)['Level'])],

        [sg.Text('Elija la duracion de la partida en minutos: ',pad=(10,10), size=(36, 1),font = ('Pixel Font7',15)),
        sg.InputCombo(('2', '3', '4', '5', '7'),background_color="old lace",pad= (70,0), size=(20, 1),key="-Time-", font = ('Pixel Font7',15) , default_value=settings_handler.get_setting(name)['Time'])],


        [sg.Text('Elija cantidad de concidencias por elemento: ', pad=(10,10), size=(36, 1),font = ('Pixel Font7',15)),
        sg.InputCombo(('2', '3', '4'),background_color="old lace", pad= (70,0), size=(20, 1),key="-Match-", font = ('Pixel Font7',15) , default_value=settings_handler.get_setting(name)['Match'])],

        [sg.Text('Elija tipo de elementos de las casillas: ', pad=(10,10), size=(36, 1), font = ('Pixel Font7',15)),
        sg.InputCombo(('Palabras', 'Imagenes'),background_color="old lace", pad= (70,0), size=(20, 1), key='-Elem-', font = ('Pixel Font7',15) , default_value=settings_handler.get_setting(name)['Elem'])],


        [sg.Text('Elija si quiere activar la ayuda o no: ', size=(36, 1), pad=(10,10) ,font = ('Pixel Font7',15)),
        sg.InputCombo(('Si', 'No'),background_color="old lace", size=(20, 1),pad = (70,0), key='-Help-', font = ('Pixel Font7',15), default_value=settings_handler.get_setting(name)['Help'])],

        [sg.Text('Elija el tema para el juego: ', size=(36, 1),pad=(10,10), font = ('Pixel Font7',15)),
        sg.InputCombo(('Dia', 'Noche', 'Tema 3') ,background_color="old lace", pad = (70,0), size=(20, 1), key='-Theme-', font = ('Pixel Font7',15) , default_value=settings_handler.get_setting(name)['Theme'])],


        [sg.Text('Ingrese frases a mostrar para las siguientes situaciones: ', size=(50, 1), pad=(100, 50), font=('Pixel Font7', 15))],

        [sg.Text('Cuando gane: ', size=(37, 1), pad=(10,10), font = ('Pixel Font7',15)), sg.InputText(key = '-TxtWin-',background_color="old lace", pad= (70,0), font = ('Pixel Font7',15),size= (20,1))],

        [sg.Text('Cuando pierda: ', size=(37, 1), pad=(10,10), font = ('Pixel Font7',15)), sg.InputText(key = '-TxtLose-',background_color="old lace", pad= (70,0), font = ('Pixel Font7',15),size= (20,1))],

        [sg.Text('Cuando quede poco tiempo: ', size=(37, 1), pad=(10,10), font = ('Pixel Font7',15)), sg.InputText(key = '-TxtTime-', pad= (70,0),background_color="old lace", font = ('Pixel Font7',15),size= (20,1))],

        [sg.Button('Aceptar',button_color=("black","grey88") ,border_width= 5, key="-Okey-",pad = ((320,0),(40,10)) , font = ('Pixel Font7',15))],
    ]

    layout = [[sg.Column(layout,justification="center")]]

    window = sg.Window('Configuracion', layout,resizable = True).finalize()

    window.maximize()
    

    return window

