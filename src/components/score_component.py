import PySimpleGUI as sg
from src.windows import score_window
from src.handlers import score_handler

def start(name):
    """ Funcion que lanza la ejecución de la ventana de puntajes """

    window = loop(name)
    window.close()
     


def loop(name):
    """ Funcion que capta los eventos de la ventana de puntajes """

    scores = score_handler.get_scores()

    window = score_window.build(scores, name)

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break

        if event == '-Accept-':
            break

        if event == '-Cancel-':
            window.close()

        if event == '-level1-':
            window.close()
            window = score_window.build(scores, name)
        
        if event == '-level2-':
            window.close()
            window = score_window.build2(scores,name)

        if event == '-level3-':
            window.close()
            window = score_window.build3(scores, name)

    return window
