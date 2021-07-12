import PySimpleGUI as sg
from src.windows import menu_window
from src.components import board_component, settings_component, stats_component, score_component
from src.handlers import settings_handler


def start(name):
    """ Funcion que lanza la ejecución de la ventana del menu """

    window = loop(name)
    window.close()


def loop(name):
    """ Funcion que capta los eventos de la ventana del menu """

    window = menu_window.build(name)

    while True:
        
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-Exit-"):
            break

        if event == "-Play-":
            window.hide()			
            board_component.start(name)     
            window.un_hide()

        if event == "-Settings-":
            window.hide()
            settings_component.start(name)
            window.un_hide()

        if event == "-Score-":
            window.hide()
            score_component.start(name)
            window.un_hide()

        if event == "-Stats-":
            window.hide()
            stats_component.start(name)
            window.un_hide()

    return window
