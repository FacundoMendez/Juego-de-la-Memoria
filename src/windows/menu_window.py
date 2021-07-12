import PySimpleGUI as sg
from src.handlers import settings_handler

def build(name):
    """ Funcion que construye la ventana del menú """

    sg.theme(settings_handler.get_theme(name))

    layout = [
        [sg.Text(('__'*300),pad=(0,70))],
        [sg.Button('Jugar',button_color=("black","grey75") ,key="-Play-",border_width= 5,  pad=(0,1),size=(40,2),font = ('Pixel Font7',16))],
        [sg.Button('Configuracion',button_color=("black","grey75"), key="-Settings-",border_width= 5,pad=(0,1),size=(40,2),font = ('Pixel Font7',16))],
        [sg.Button('Puntajes',button_color=("black","grey75"), key="-Score-",border_width= 5,pad=(0,1),size=(40,2),font = ('Pixel Font7',16))],
        [sg.Button('Estadisticas',button_color=("black","grey75"), key="-Stats-",border_width= 5,pad=(0,1),size=(40,2),font = ('Pixel Font7',16))],
        [sg.Button('Salir',button_color=("black","grey75"), key="-Exit-",border_width= 5,pad=(0,1),size=(40,2),font = ('Pixel Font7',16))],
        [sg.Text(('__'*300),pad=(0,60))]
    ]

    layout = [[sg.Column(layout,element_justification="center")]]
    

    window = sg.Window('MemPy', layout, resizable = True).Finalize()
    window.maximize()
    
    window['-Play-'].set_cursor(cursor='hand2')
    window['-Settings-'].set_cursor(cursor='hand2')
    window['-Score-'].set_cursor(cursor='hand2')
    window['-Stats-'].set_cursor(cursor='hand2')
    window['-Exit-'].set_cursor(cursor='hand2')

    return window

 


    