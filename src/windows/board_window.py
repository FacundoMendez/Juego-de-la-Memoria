import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import set_options
from src.handlers import settings_handler


def build(name,time,board_data,rows,columns):
    """ Funcion que construye la ventana del tablero del juego """

    sg.theme(settings_handler.get_theme(name))
    
    if columns == 4:
        level= "FACIL"
    if columns == 8:
        level= "MEDIO"
    if columns== 12:
        level= "DIFICIL"

    layout = [
        [sg.Text(f'JUGADOR: {name}', size=(17, 1), justification="center", text_color='#ff0055',
                 font=('Pixel Font7', 15))],
        [sg.Text(f'Nivel: {level}  --  Tiempo total: {time} min', size=(34, 1), justification="right",
                 text_color='#ff0055', font=('Pixel Font7', 15))],
        [sg.Text("", size=(17, 1), justification="center", key="-Timer-", text_color='#ff0055',
                 font=('Pixel Font7', 15), )],
    ]

    if level == "FACIL":
        for x in range(rows):
            layout += [
                [

                    sg.Button(board_data[x][y] ,button_color=('#ff0055', "#080010"), font=('Pixel Font7', 13),
                              border_width=4, size=(10, 3), key=f'cell-{x}-{y}')
                    for y in range(columns)
                ]
            ]

    if level == "MEDIO":
        for x in range(rows):
            layout += [
                [

                    sg.Button(board_data[x][y], button_color=('#ff0055', "#080010"), font=('Pixel Font7', 13),
                              border_width=2, size=(10, 3), key=f'cell-{x}-{y}')
                    for y in range(columns)
                ]
            ]

    if level == "DIFICIL":
        for x in range(rows):
            layout += [
                [

                    sg.Button(board_data[x][y], button_color=('#ff0055', "#080010"), font=('Pixel Font7', 13),
                              border_width=2, size=(9, 3), key=f'cell-{x}-{y}')
                    for y in range(columns)
                ]
            ]

    layout += [
        [sg.Button('SALIR', button_color=("black", "grey85"), pad=((0, 0), (25, 10)), key='-BACK-', border_width=5,
                   font=('Pixel Font7', 16))],
    ]

    layout = [[sg.Column(layout, element_justification="c", justification="center")]]

    window = sg.Window("Tablero MemPy", layout, resizable=True).Finalize()
    window.maximize()
    window['-BACK-'].set_cursor(cursor='hand2')

    return window