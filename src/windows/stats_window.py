import PySimpleGUI as sg
from src.handlers import settings_handler

def build(name):
    """ Funcion que construye la ventana de estadisticas """

    sg.theme(settings_handler.get_theme(name))

    layout = [
        [sg.Text('ESTADISTICAS: ', size=(17, 1), font = ('Pixel Font7',15),pad=((60,0),(40,0)))],
        [sg.Button('Partidas terminadas, canceladas, abandonadas ', button_color=('#ff0055', '#080010'), pad=((10,0),(120,0)), font=('Pixel Font7', 14), border_width=4, key="-Estado-")],
        [sg.Button('Partidas finalizadas según género', button_color=('#ff0055', '#080010'), pad=((10,0),(50,0)), font=('Pixel Font7', 14), border_width=4, key="-Finalizadas-")],
        [sg.Button('Palabras que mas veces se encuentran', button_color=('#ff0055', '#080010'), pad=((10,0),(50,0)), font=('Pixel Font7', 14), border_width=4, key="-Palabras-")],
        [sg.Button('Aceptar', button_color=("black","grey85"),key = '-Accept-',border_width= 5,pad=((10,0),(120,0)), font = ('Pixel Font7',15)),
        sg.Button('Volver', button_color=("black","grey85"),key = '-Cancel-',border_width= 5,pad=((10,0),(120,0)), font = ('Pixel Font7',15))]
    ]

    layout = [[sg.Column(layout, element_justification="c", justification="center")]]
    
    window = sg.Window('Estadisticas', layout, resizable = True).Finalize()
    window.maximize()

    window['-Accept-'].set_cursor(cursor='hand2')
    window['-Cancel-'].set_cursor(cursor='hand2')
    return window



 
