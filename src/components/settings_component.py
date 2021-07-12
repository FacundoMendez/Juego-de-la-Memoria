import PySimpleGUI as sg
from src.windows import settings_window
from src.handlers import settings_handler


def start(name):
    """ Funcion que lanza la ejecución de la ventana de configuracion """

    window = loop(name)
    window.close()


def loop(name):
    """ Funcion que capta los eventos de la ventana de configuracion """

    window = settings_window.build(name)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break

        if event == "-Okey-":

            settings_handler.general(name, values)

            if values ["-TxtWin-"]:
                settings_handler.txtwin(name, values)

            if values ["-TxtLose-"]:
                settings_handler.txtlos(name, values)

            if values ["-TxtTime-"]:
                settings_handler.txttime(name, values)

            break

    return window
