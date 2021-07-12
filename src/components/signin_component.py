import PySimpleGUI as sg
from src.handlers import signin_handler
from src.windows import signin_window


def start():
    """ Funcion que lanza la ejecucion de la ventana del registro """

    window = loop()
    window.close()


def loop():
    """ Funcion que capta los eventos de la ventana del registro """

    window = signin_window.build()

    while True:

        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == '-Accept-':
            
            if (values['-User-'] != "") and (values['-Gender-'] != "") and (values['-Age-'] != ""):

                if signin_handler.load_user(values['-User-'],values['-Gender-'],values['-Age-']):
                    sg.popup(f"""
Gracias por registrarte: {values['-User-']}
                    """,grab_anywhere=True,button_color=('#ff0055','#0d011a'),background_color="#080010",text_color= "white",font = ('Pixel Font7',18),no_titlebar=True)
                    window.close()
                    break
                else:
                     sg.popup(f"""
Perdon, el nombre de usuario '{values['-User-']}' ya existe! 

        por favor ingrese otro.
                    """,grab_anywhere=True,button_color=('#ff0055','#0d011a'),background_color="#080010",text_color= "white",font = ('Pixel Font7',18),no_titlebar=True)
            else:
                  sg.popup("""
Por favor, rellene todos los campos correspondientes!
                """,grab_anywhere=True,button_color=('#ff0055','#0d011a'),background_color="#080010",text_color= "white",font = ('Pixel Font7',18),
    no_titlebar=True)

        if event == '-Cancel-':
            window.close()


    return window