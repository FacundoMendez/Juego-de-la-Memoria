import PySimpleGUI as sg
from src.windows import login_window
from src.components import menu_component, signin_component
from src.handlers import login_handler


def start():
    """ Funcion que lanza la ejecucion de la ventana del login """

    window = loop()
    window.close()


def loop():
    """ Funcion que capta los eventos de la ventana del login """

    window = login_window.build()

    while True:

        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == '-Login-':
            if login_handler.check_user(values['-User-']): 
                sg.popup(f" Bienvenido {values['-User-']} !",grab_anywhere=True,background_color="#080010",button_color=('#ff0055','#0d011a'),text_color= "white",font = ('Pixel Font7',18),no_titlebar=True)
                window.close()
                menu_component.start(values['-User-'])
            else:
                sg.popup("""
Ups! Parece que no estas registrado! 

Por favor, registrate para continuar.
                """,grab_anywhere=True,background_color="#080010",button_color=('#ff0055','#0d011a'),text_color= "white",font = ('Pixel Font7',18),
    no_titlebar=True)

        if event == '-SignIn-':
            window.hide()
            signin_component.start()
            window.un_hide()

    return window

