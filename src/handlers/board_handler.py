import time as t

def crear(data,rows,columns):
    """Crea el tablero a usar"""

    armado = [[''] * columns for i in range(rows)]

    i = 0

    for x in range(rows):
        for y in range(columns):
            armado[x][y] = data[i]
            i += 1

    return armado
    

def play (window, event, board_data, armado):
    """Muestra ficha volteada y establece el criterio a buscar"""

    _prefix, x, y = event.split("-")
    window[event].update(armado[int(x)][int(y)])
    actual=armado[int(x)][int(y)]

    return board_data, actual


def play2 (window, event, board_data, armado, acierto, actual):
    """Muestra ficha volteada y establece si hay acierto o no"""

    _prefix, x, y = event.split("-")
    window[event].update(armado[int(x)][int(y)])
    if (actual!=armado[int(x)][int(y)]):
        acierto=False
    return board_data, acierto


def ocultar(window, board_data, volteados):
    """Oculta las fichas en caso de que se hayan tocado algunas que no sean del mismo conjunto"""
    inicio = t.time()
    time = t.time() - inicio
    while int(time % 60) < 1:
        time = t.time() - inicio
    for i in range(len(volteados)):
        a = (volteados[i])
        window[a].update(" ")

    return board_data