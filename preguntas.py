"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

from collections import Counter
with open('data.csv','r') as file:  
  datos=file.readlines()
  datos=[row.replace('\n','') for row in datos]
  datos=[row.split('\t') for row in datos]
  

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    datos1=[row[1] for row in datos]
    datos1=[int(x) for x in datos1]
    suma=0
    for i in datos1[:]:
        suma += i
    
    return suma



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    datos2=[row[0] for row in datos]
    Result=Counter(datos2).most_common()
    Result.sort(reverse=False)
    
    return Result



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    datos1=[row[1] for row in datos]
    datos1=[int(x) for x in datos1]

    datos2=[row[0] for row in datos]
    L=list(set(datos2))
    L.sort(reverse=False)

    datos3=[0]*len(L)
    R3=[0]*len(L)

    for a in range(0,len(L)):
      for k in range(0,len(datos1)):
       if datos2[k]==L[a]:
        datos3[a] += datos1[k]
        R3[a]=L[a],datos3[a]

    return R3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    Fecha=[row[2] for row in datos]
    Fecha=[row.split('-') for row in Fecha]
    date=[row[1] for row in Fecha]


    R4=Counter(date).most_common()
    R4.sort(reverse=False)

    return R4


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    datos1=[int(row[1]) for row in datos]
    datos2=[row[0] for row in datos]
    L=list(set(datos2))
    L.sort(reverse=False)

    Maximo=[0]*len(L)
    Minimo=[max(datos1)]*len(L)
    R5=[0]*len(L)

    for i in range(0,len(L)):
      for j in range(0,len(datos1)):
        if datos2[j]==L[i]:
            if datos1[j] > Maximo[i]:
                Maximo[i]=datos1[j]
            if datos1[j] < Minimo[i]:
                Minimo[i]=datos1[j]
        R5[i]=L[i],Maximo[i],Minimo[i]    


    return R5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    col5=[row[4].split(',') for row in datos]

    col5=[elem for row in col5 for elem in row]
    col5=[row.split(':') for row in col5]



    con=list(set([row[0] for row in col5]))
    con.sort(reverse=False)
    my_list=list(zip((row[0] for row in col5),(int(z[1]) for z in col5)))

    max=[0]*len(con)
    min=[my_list[0][1]]*len(con)
    R6=[0]*len(con)
    for r in range(0,len(con)):
        for h in range(0,len(my_list)):
            if con[r]==my_list[h][0]:
                if my_list[h][1]>max[r]:
                    max[r]=my_list[h][1]
                if my_list[h][1]<min[r]:
                    min[r]=my_list[h][1]
        R6[r]=con[r],min[r],max[r]

    return R6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    datos1=[int(row[1]) for row in datos]
    datos2=[row[0] for row in datos]


    lista7=list(set(datos1))
    col12=list(zip(datos1,datos2))

    R7=[0]*len(lista7)

    for row in lista7:
        letters=[]
        for m in range(0,len(col12)):
            if row==col12[m][0]:
                letters +=col12[m][1]
                R7[row]=lista7[row],letters


    return R7


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    datos1=[int(row[1]) for row in datos]
    datos2=[row[0] for row in datos]

    lista7=list(set(datos1))
    col12=list(zip(datos1,datos2))

    R8=[0]*len(lista7)

    for row in lista7:
      letters=[]
      for m in range(0,len(col12)):
            if row==col12[m][0]:
                letters +=col12[m][1]
                Orden=list(set(letters))
                Orden.sort(reverse=False)

      R8[row]=lista7[row],Orden


    return R8


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    col5=[row[4].split(',') for row in datos]

    col5=[elem for row in col5 for elem in row]
    col5=[row.split(':') for row in col5]

    coletra=[row[0] for row in col5]
    R9=Counter(coletra)

    return R9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    datos2=[row[0] for row in datos]
    co5=[row[4].split(',') for row in datos]
    co4=[row[3].split(',') for row in datos]
    cont5=[0]*len(co5)
    cont4=[0]*len(co4)
    for i in range(0,len(co5)):
        for j in range(0,len(co5[i])):
            cont5[i] +=1
    
    for x in range(0,len(co4)):
        for z in range(0,len(co4[x])):
            cont4[x] +=1

    
    R10=list(zip(datos2,cont4,cont5))

    return R10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data=[row[3]+'-'+row[1] for row in datos]
    data=[row.split('-') for row in data]
    datal=[row[0].split(',') for row in data]
    data1=[datal[row][ele]+','+data[row][1] for row in range(0,len(datal)) for ele in range(0,len(datal[row]))]

    datat=[row.split(',') for row in data1]
    R11={}

    for letter,value in datat:
      value=int(value)
      if letter in R11.keys():
        R11[letter].append(value)
      else:
        R11[letter]=[value]

    R11=dict((key, sum(value)) for key,value in R11.items())

    return R11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    datos2=[row[0] for row in datos]
    col5=[row[4].replace(':',',') for row in datos]
    col5=[row.split(',') for row in col5]
    col6=[row[1::2] for row in col5]

    T12=[]

    for x in col6:
        dato=[]
        for z in x:
            dato.append(int(z))
        T12.append(dato)
    
    conj=list(zip(datos2,T12))
    cont=list(set(datos2))
    cont.sort(reverse=False)
    contador=[0]*len(cont)
    for a in range(0,len(cont)):
        for n,m in conj:
            if n==cont[a]:
                contador[a]=contador[a]+sum(m)

        R12=dict(zip(cont,contador))  


    return R12
