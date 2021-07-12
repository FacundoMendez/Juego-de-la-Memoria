import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import set_options
from src.handlers import settings_handler



def build(scores, name):
    """ Funcion que construye la ventana de puntajes """

    sg.theme(settings_handler.get_theme(name))

    firstList = scores["6x4"]

    layout = [
        [sg.Text('TABLA DE PUNTUACIÓN: ', font = ('Pixel Font7',20),pad= ((0,0),(50,50)))],
        [sg.Text('Posicion: ', font = ('Pixel Font7',15),pad= ((0,100),(0,20))),
        sg.Text('Nombre: ',font = ('Pixel Font7',15),pad= ((0,100),(0,20))),
        sg.Text('Puntaje:',font = ('Pixel Font7',15),pad= ((0,0),(0,20)))]
    ]

    i=1
    for score in range(0,10):
        try:
            layout += [       
                [sg.Text(f"{i}",font = ('Pixel Font7',13),pad= ((0,100),(0,10))),
                sg.Text(f"{firstList[score][0]} ",pad= ((60,0),(0,0)),font = ('Pixel Font7',13),size= (21,0)),
                sg.Text(f"{firstList[score][1]}",pad= ((0,0),(0,0)),font = ('Pixel Font7',13))],
            ]
        except IndexError:
            break
        i +=1   
     
    while i <= 10:
        layout += [       
        [sg.Text(f"{i}",font = ('Pixel Font7',13),pad= ((0,100),(0,10))),
         sg.Text("--- ",pad= ((60,0),(0,0)),font = ('Pixel Font7',13),size= (21,0)),
         sg.Text("---",pad= ((0,0),(0,0)),font = ('Pixel Font7',13))],
        ]
        i += 1 


    layout += [
        [sg.Button('Nivel: FACIL ',button_color=('#ff0055','#080010'),font = ('Pixel Font7',14),border_width= 4 ,key= "-level1-",pad=((20,0),(50,0))),
         sg.Button('Nivel: MEDIO ',button_color=('#ff0055','#080010'),font = ('Pixel Font7',14),border_width= 4,key= "-level2-",pad=((20,0),(50,0))),
         sg.Button('Nivel: DIFICIL ',button_color=('#ff0055','#080010'),font = ('Pixel Font7',14),border_width= 4,key= "-level3-",pad=((20,0),(50,0)))]
    ]
   
    layout += [
        [sg.Button('Aceptar', button_color=("black","grey85"),key = '-Accept-',border_width= 5,pad=((0,20),(30,0)), font = ('Pixel Font7',15)),   
        sg.Button('Volver', button_color=("black","grey85"),key = '-Cancel-',border_width= 5,pad=((0,20),(30,0)), font = ('Pixel Font7',15))]
    ]
    

    layout = [[sg.Column(layout,justification="center",element_justification="c")]]
    
    window = sg.Window('score', layout, resizable = True).Finalize()
    window.maximize()

    window['-Accept-'].set_cursor(cursor='hand2')
    window['-Cancel-'].set_cursor(cursor='hand2')
    return window


def build2(scores, name):
    """ Funcion que construye la ventana de puntajes """

    sg.theme(settings_handler.get_theme(name))

    secondList = scores["6x8"]

    layout = [
        [sg.Text('TABLA DE PUNTUACIÓN: ', font = ('Pixel Font7',20),pad= ((0,0),(50,50)))],
        [sg.Text('Posicion: ', font = ('Pixel Font7',15),pad= ((0,100),(0,20))),
        sg.Text('Nombre: ',font = ('Pixel Font7',15),pad= ((0,100),(0,20))),
        sg.Text('Puntaje:',font = ('Pixel Font7',15),pad= ((0,0),(0,20)))]
    ]

    i=1
    for score in range(0,10):
        try:
            layout += [       
                [sg.Text(f"{i}",font = ('Pixel Font7',13),pad= ((0,100),(0,10))),
                sg.Text(f"{secondList[score][0]} ",pad= ((60,0),(0,0)),font = ('Pixel Font7',13),size= (21,0)),
                sg.Text(f"{secondList[score][1]}",pad= ((0,0),(0,0)),font = ('Pixel Font7',13))],
            ]
        except IndexError:
            break
        i +=1    

    while i <= 10:
        layout += [       
        [sg.Text(f"{i}",font = ('Pixel Font7',13),pad= ((0,100),(0,10))),
         sg.Text("--- ",pad= ((65,0),(0,0)),font = ('Pixel Font7',13),size= (21,0)),
         sg.Text("---",pad= ((0,0),(0,0)),font = ('Pixel Font7',13))],
        ]
        i += 1 


    layout += [
        [sg.Button('Nivel: FACIL ',button_color=('#ff0055','#080010'),font = ('Pixel Font7',15),border_width= 4, key= "-level1-",pad=((20,0),(50,0))),
        sg.Button('Nivel: MEDIO ',button_color=('#ff0055','#080010'),font = ('Pixel Font7',15),border_width= 4,key= "-level2-",pad=((20,0),(50,0))),
        sg.Button('Nivel: DIFICIL ',button_color=('#ff0055','#080010'),font = ('Pixel Font7',15),border_width= 4,key= "-level3-",pad=((20,0),(50,0)))]
    ]
   
    layout += [
        [sg.Button('Aceptar', button_color=("black","grey85"),key = '-Accept-',border_width= 5,pad=((20,0),(30,0)), font = ('Pixel Font7',15)),   
        sg.Button('Volver', button_color=("black","grey85"),key = '-Cancel-',border_width= 5,pad=((20,0),(30,0)), font = ('Pixel Font7',15))]
    ]

    layout = [[sg.Column(layout,justification="center",element_justification="c")]]
    
    window = sg.Window('score', layout, resizable = True).Finalize()
    window.maximize()

    window['-Accept-'].set_cursor(cursor='hand2')
    window['-Cancel-'].set_cursor(cursor='hand2')
    return window


def build3(scores, name):
    """ Funcion que construye la ventana de puntajes """

    sg.theme(settings_handler.get_theme(name))

    thirdList = scores["6x12"]

    layout = [
        [sg.Text('TABLA DE PUNTUACIÓN: ', font = ('Pixel Font7',20),pad= ((0,0),(50,50)))],
        [sg.Text('Posicion: ', font = ('Pixel Font7',15),pad= ((0,100),(0,20))),
        sg.Text('Nombre: ',font = ('Pixel Font7',15),pad= ((0,100),(0,20))),
        sg.Text('Puntaje:',font = ('Pixel Font7',15),pad= ((0,0),(0,20)))]
    ]

    i=1
    for score in range(0,10):
        try:
            layout += [       
                [sg.Text(f"{i}",font = ('Pixel Font7',13),pad= ((0,100),(0,10))),
                sg.Text(f"{thirdList[score][0]} ",pad= ((60,0),(0,0)),font = ('Pixel Font7',13),size= (21,0)),
                sg.Text(f"{thirdList[score][1]}",pad= ((0,0),(0,0)),font = ('Pixel Font7',13))],
            ]
        except IndexError:
            break
        i +=1    

    while i <= 10:
        layout += [       
        [sg.Text(f"{i}",font = ('Pixel Font7',13),pad= ((0,100),(0,10))),
         sg.Text("--- ",pad= ((50,0),(0,0)),font = ('Pixel Font7',13),size= (21,0)),
         sg.Text("---",pad= ((0,0),(0,0)),font = ('Pixel Font7',13))],
        ]
        i += 1 


    layout += [
        [sg.Button('Nivel: FACIL ',button_color=('#ff0055','#080010'),font = ('Pixel Font7',15),border_width= 4, key= "-level1-",pad=((0,0),(50,0))),
        sg.Button('Nivel: MEDIO ',button_color=('#ff0055','#080010'),font = ('Pixel Font7',15),border_width= 4,key= "-level2-",pad=((20,20),(50,0))),
        sg.Button('Nivel: DIFICIL ',button_color=('#ff0055','#080010'),font = ('Pixel Font7',15),border_width= 4,key= "-level3-",pad=((0,0),(50,0)))]
    ]
   
    layout += [
        [sg.Button('Aceptar', button_color=("black","grey85"),key = '-Accept-',border_width= 5,pad=((20,0),(30,0)), font = ('Pixel Font7',15)),   
        sg.Button('Volver', button_color=("black","grey85"),key = '-Cancel-',border_width= 5,pad=((20,0),(30,0)), font = ('Pixel Font7',15))]
    ]
    

    layout = [[sg.Column(layout,justification="center",element_justification="c")]]
    
    window = sg.Window('score', layout, resizable = True).Finalize()
    window.maximize()

    window['-Accept-'].set_cursor(cursor='hand2')
    window['-Cancel-'].set_cursor(cursor='hand2')
    return window
