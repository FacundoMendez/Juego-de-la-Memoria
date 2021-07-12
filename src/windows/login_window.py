import PySimpleGUI as sg


def build():
    """ Funcion que construye la ventana del login """
    
    sg.theme('Darkpurple1') 
    layout = [
        [sg.Text(('__'*300),pad=(0,70))],
        [sg.Text('Bienvenido ', pad=(0,40), font = ('Pixel Font7',35))],
        [sg.Text('Usuario: ' ,pad=(0,20),font = ('Pixel Font7',22)), sg.InputText(key = '-User-',background_color="old lace",font = ('Pixel Font7',18),size= (30,0)), sg.Button('Iniciar',button_color=("black","grey85"),border_width= 4 ,key = '-Login-',font = ('Pixel Font7',14))],
        [sg.Button('Registrarse',button_color=("black","grey85"),pad=(0,50),size= (0,0),key = '-SignIn-',border_width= 4,font = ('Pixel Font7',15))],
        [sg.Text(('__'*300),pad=(0,20))]
    ]

    layout = [[sg.Column(layout,element_justification="center")]]
    

    window = sg.Window('Inicio', layout, resizable = True).Finalize()
    window.maximize()
    window['-Login-'].set_cursor(cursor='hand2')
    window['-SignIn-'].set_cursor(cursor='hand2')

    return window  