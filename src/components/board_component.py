import PySimpleGUI as sg
import time as t
import os.path

from src.windows import board_window
from src.handlers import board_handler, settings_handler, data_handler, score_handler


def start(name):
    """ Funcion que lanza la ejecución de la ventana del tablero """

    window = loop(name)
    window.close()


def loop(name):
    """ Funcion que capta los eventos de la ventana del tablero """

    data = data_handler.get_data(name)
    level = settings_handler.get_level(name)
    minutes = settings_handler.get_time(name)

    board_data = [[" "] * (level[1]) for _i in range(level[0])]
    armado = board_handler.crear(data,level[0],level[1])

    window = board_window.build(name,minutes,board_data,level[0],level[1])

    answer = sg.popup_yes_no("""Quiere iniciar el Juego?""",grab_anywhere=True,button_color=('#ff0055','#0d011a'),background_color="#0f0024",text_color= "white",font = ('Pixel Font7',18),
    no_titlebar=True)

    if answer == 'No':
        window.close()

    path_files = "src/files"
    path_arch = os.path.join(os.getcwd(), path_files)
    archivo = "estadisticas.csv"
    csv = open(os.path.join(path_arch, archivo), 'a', encoding='utf-8')
    genero = settings_handler.get_setting(name)['Gender']
    edad = settings_handler.get_setting(name)['Age']

    start_time = t.time()
    cant_coincidencias = 0
    acierto = True
    volteados = []
    volteados_correctos = []
    cant_aciertos = 0
    level = settings_handler.get_level(name)
    elements = level[0] * level[1]
    cant_aciertos_ganar = elements/int(settings_handler.get_setting(name)['Match'])
    tablero_desbloq = True

    if level==[6, 4]:
        puntaje = 1000
        nivel = "Facil"
    elif level==[6, 8]:
        puntaje = 3000
        nivel = "Medio"
    else:
        puntaje = 5000
        nivel ="Dificil"

    fila = str(int(t.time())) + "," + 'Partida n' + "," + str(cant_aciertos_ganar) + "," + 'Inicio_Partida' + "," + str(
        name) + "," + genero + "," + edad + "," + "-" + "," + "-" + "," + str(nivel) + "\n"
    csv.write(fila)

    while True:
        event, values = window.read(timeout=100)

        if event == sg.WINDOW_CLOSED:
            fila = str(int(t.time())) + "," + 'Partida n' + "," + str(
                cant_aciertos_ganar) + "," + 'Fin_Partida' + "," + str(
                name) + "," + genero + "," + edad + "," + "Cancelada" + "," + "-" + "," + str(nivel) + "\n"
            csv.write(fila)
            window.close()
            break

        #Si es la segunda, tercera o cuarta ficha de ese conjunto que se da vuelta
        if event.startswith("cell") and (cant_coincidencias > 0) and (cant_coincidencias<int(settings_handler.get_setting(name)['Match'])) and (tablero_desbloq == True) and not (
                event in volteados) and not (
                event in volteados_correctos):
            tablero_desbloq = False
            volteados.append(event)
            board_data, acierto = board_handler.play2(window, event, board_data, armado, acierto, actual)
            cant_coincidencias = cant_coincidencias+ 1

        #Si es la primera ficha de ese conjunto que se da vuelta
        if event.startswith("cell") and (cant_coincidencias==0) and not (event in volteados_correctos):
            volteados.append(event)
            board_data, actual = board_handler.play(window, event, board_data, armado)
            cant_coincidencias=cant_coincidencias+1
            fila = str(int(t.time())) +","+'Partida n'+","+str(cant_aciertos_ganar)+","+'Primera_Ficha'+","+str(name)+","+ genero + "," + edad +","+"Primera"+","+str(actual)+","+str(nivel)+"\n"
            csv.write(fila)

        window.refresh()

        #Si se completó un conjunto de fichas iguales
        if (cant_coincidencias == int(settings_handler.get_setting(name)['Match'])) and (acierto==True):
            for i in range(len(volteados)):
                volteados_correctos.append(volteados[i])
            volteados = []
            cant_coincidencias = 0
            cant_aciertos = cant_aciertos + 1
            fila = str(int(t.time())) + "," + 'Partida n' + "," + str(cant_aciertos_ganar) + "," + 'Conjunto_Correcto' + "," + str(
                name) + "," + genero + "," + edad + "," + "Correcto" + "," + str(actual) + "," + str(nivel) + "\n"
            csv.write(fila)

        #Si se volteó una ficha equivocada
        if (acierto == False):
            board_handler.ocultar(window, board_data, volteados)
            volteados = []
            acierto = True
            cant_coincidencias = 0
            puntaje=puntaje-10
            fila = str(int(t.time())) + "," + 'Partida n' + "," + str(cant_aciertos_ganar) + "," + 'Conjunto_Incorrecto' + "," + str(
                name) + "," + genero + "," + edad + "," + "Error" + "," + str(actual) + "," + str(nivel) + "\n"
            csv.write(fila)

        tablero_desbloq = True

        #Si ganaste
        if (cant_aciertos_ganar == cant_aciertos):
            puntaje= puntaje - 120 * int(current_time // 60) - 2*(int(current_time % 60))
            sg.popup(f"""
            {settings_handler.get_setting(name)['TxtWin']}! Tu puntaje es:  {puntaje}!
                        """, grab_anywhere=True, button_color=('#ff0055', '#0d011a'), background_color="#0f0024", text_color="white", font=('Pixel Font7', 20), no_titlebar=True)
            score_handler.save_score(name, level, puntaje)
            fila = str(int(t.time())) + "," + 'Partida n' + "," + str(cant_aciertos_ganar) + "," + 'Fin_Partida' + "," + str(
                name) + "," + genero + "," + edad + "," + "Ganada" + "," + str(actual) + "," + str(nivel) + "\n"
            csv.write(fila)
            break

        if event == '-BACK-':
            window.close()

        current_time = t.time() - start_time
        window["-Timer-"].update(f"{round(current_time // 60):02d}:{round(current_time % 60):02d}")

        #Si se acabó el tiempo
        if int(current_time // 60)>=int(settings_handler.get_setting(name)['Time']):
            sg.popup(f"""
            {settings_handler.get_setting(name)['TxtLose']}
                    """, grab_anywhere=True, button_color=('#ff0055', '#0d011a'), background_color="#0f0024",
                     text_color="white", font=('Pixel Font7', 20),
                     no_titlebar=True)
            fila = str(int(t.time())) + "," + 'Partida n' + "," + str(cant_aciertos_ganar) + "," + 'Fin_Partida' + "," + str(
                name) + "," + genero + "," + edad + "," + "Sin_Tiempo" + "," + str(actual) + "," + str(nivel) + "\n"
            csv.write(fila)
            break

        #Si te queda poco tiempo
        if int(current_time // 60)==(int(settings_handler.get_setting(name)['Time'])-1) and (int (current_time % 60)==0):
            sg.popup(f"""
            {settings_handler.get_setting(name)['TxtTime']}
                    """, grab_anywhere=True, background_color="#0f0024", button_color=('#ff0055', '#0d011a'),
                     text_color="white", font=('Pixel Font7', 20),
                     no_titlebar=True)

    return window
