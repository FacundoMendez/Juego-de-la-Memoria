import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os.path


path_files = "src/files"
path_arch = os.path.join(os.getcwd(), path_files)
archivo = "estadisticas.csv"
data_set = pd.read_csv(os.path.join(path_arch, archivo))


def firstGraphic():
    """ Porcentaje de partidas por estado (terminada, cancelada, abandonadas). """

    plt.clf()

    grupos = data_set.groupby([' Estado'])[' Estado'].count()

    etiquetas = ["Sin tiempo", "Ganada", "Cancelada"]
    data_dibujo = [grupos["Sin_Tiempo"], grupos["Ganada"], grupos["Cancelada"]]
    plt.pie (data_dibujo, labels = etiquetas, autopct = '%1.1f%%', shadow=True, startangle=90, labeldistance = 1.1)
    plt.legend (etiquetas)
    plt.title ('Porcentaje de partidas por estado')
    #plt.savefig('primerGrafico.png')
    plt.show()
    #return 'primerGrafico.png'



def secondGraphic():
    """ Gráfico que muestre el porcentaje de partidas finalizadas según género. """

    plt.clf()

    f = data_set [(data_set[' Estado']=='Ganada') & (data_set[' Genero']=='Femenino')] [' Genero'].count()
    m = data_set [(data_set[' Estado']=='Ganada') & (data_set[' Genero']=='Masculino')] [' Genero'].count()
    o = data_set [(data_set[' Estado']=='Ganada') & (data_set[' Genero']=='Otro')] [' Genero'].count()

    data_dibujo_2 = [f, m, o]
    etiquetas_2 = ["Femenino", "Masculino", "Otro"]
    plt.pie (data_dibujo_2, labels = etiquetas_2, autopct = '%1.1f%%', shadow=True, startangle=90, labeldistance = 1.1)
    plt.legend (etiquetas_2)
    plt.title ('Porcentaje de partidas finalizadas por genero')
    #plt.savefig('segundoGrafico.png')
    plt.show()
    #return 'segundoGrafico.png'



def thirdGraphic():
    """ Grafico que muestra las 10 palabras que mas veces se encuentran en el juego """

    plt.clf()

    palabras = data_set[' Palabra'].value_counts()
    del(palabras['-'])
    first_ten = palabras[:10]

    first_ten.plot(kind='bar')
    plt.title ('10 palabras que mas veces se encuentran en el juego')
    fig = plt.gcf()
    fig.set_size_inches(11, 4)
    #plt.savefig('tercerGrafico.png')
    plt.show()
    #return 'tercerGrafico.png'