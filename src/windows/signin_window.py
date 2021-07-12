import PySimpleGUI as sg

def build():
    """ Funcion que construye la ventana del registro """

    sg.theme('Darkpurple1')   

    layout = [
        [sg.Text(('__'*300),pad=(0,60))],

        [sg.Text('Ingrese sus datos: ',pad=(0,30),font = ('Pixel Font7',25))],

        [sg.Text('Nombre de Usuario: ',pad=(0,10), font = ('Pixel Font7',18)),sg.InputText(key = '-User-',background_color="old lace",pad = ((8,160),(15,15)))],

        [sg.Text('Genero: ',font = ('Pixel Font7',18)),   sg.InputCombo(('Femenino', 'Masculino', 'Otro'),background_color="old lace",pad = ((0,38),(15,15))  ,size=(43,0),key="-Gender-")],

        [sg.Text('Edad: ', font = ('Pixel Font7',18)),   sg.InputText(key = '-Age-',background_color="old lace",pad = ((0,13),(15,15)))],

        [sg.Button('Aceptar', button_color=("black","grey85"),key = '-Accept-',pad=(0,30),border_width= 5, font = ('Pixel Font7',15)),   sg.Button('Volver', button_color=("black","grey85"),key = '-Cancel-',border_width= 5,pad=(20,30), font = ('Pixel Font7',15))],
        
        [sg.Text(('__'*300),pad=(0,50))]
    ]

    layout = [[sg.Column(layout,element_justification = "center")]]
    
    window = sg.Window('MemPy', layout, resizable = True).Finalize()
    window.maximize()

    window['-Accept-'].set_cursor(cursor='hand2')
    window['-Cancel-'].set_cursor(cursor='hand2')
    return window
