import PySimpleGUI as sg
from src.windows import stats_window
from src.handlers import stats_handler

def start(name):
    """ Funcion que lanza la ejecución de la ventana de estadisticas """

    window = loop(name)
    window.close()

def loop(name):
    """ Funcion que capta los eventos de la ventana de estadisticas """

    window = stats_window.build(name)

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break

        if event == '-Estado-':
            stats_handler.firstGraphic()

        if event == '-Finalizadas-':
            stats_handler.secondGraphic()

        if event == '-Palabras-':
            stats_handler.thirdGraphic()

        if event == '-Accept-':
            break
        
        if event == '-Cancel-':
            window.close()

    return window

