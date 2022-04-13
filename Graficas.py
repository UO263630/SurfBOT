"""
-Clase: Graficas.py
-Descripción: Clase en la cual se crean las funciones que dibujan las graficas
    que el bot manda a los usuarios periodicamente. Ademas de estas funciones
    tambien existe una función auxiliar para el coloreado de las gráficas
"""

#Libreria para funciones matematicas de alto nivel
import numpy as np

#Libreria para el diseño de gráficas
import matplotlib.pyplot as plt


#Función que va recibiendo la temperatura para cada valor de la gráfica
#y en función de este le otorga un color determinado
def colors(t):
    if(t<=0):
        return 'royalblue'
    if(t>0 and t<=5):
        return 'turquoise'
    if(t>5 and t<=10):
        return 'mediumspringgreen'
    if(t>10 and t<=15):
        return 'limegreen'
    if(t>15 and t<=20):
        return 'lightsalmon'
    if(t>20 and t<=25):
        return 'salmon'
    if(t>25 and t<=30):
        return 'orange'
    if(t>30 and t<=35):
        return 'orangered'
    if(t>35 and t<=40):
        return 'firebrick'
    if(t>40 and t<=45):
        return 'red'
    else:
        return 'darkred'
    



#Función que crea una gráfica con los datos de dirección de viento y lo guarda en una imagen.
#Ah esta función se le pasan tres argumentos:
#   -grados: vector con la direccion del viento para las horas establecidas
#   -aux: variable auxiliar que indica si la grafica es para el dia actual o para 
#   -tem: vector con la temperatura del aire para las horas establecidas
def grafica1(grados,aux,tem):
    print(grados)
    print(tem)
    if(len(grados)==13):
        x= np.linspace(0,24,13)
        ejex=["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00","00:00"]
   
    else:
        x = np.linspace(1, 23, 12)
        ejex=["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00"]
   


    fig = plt.figure()
    fig.set_size_inches(8,2)
    ax = fig.gca()
    #print(x)
    #print(np.zeros(x.shape))

    print(tem)
    t=[]

    characters=" ºC"
    i=0
    for z in tem:
      t.append(''.join(y for y in z if y not in characters))
      t[i]=float(t[i])
      i=i+1
      

    a=[]
    i=0
    print("--------------------------------------------")


    while(i<len(grados)):
        b=-np.tan(grados[i])*x[i]
        a.append(1-b)
        i=i+1;

    print(len(x))
    #print(a)
    plt.xticks(x,ejex)
    plt.xlabel("horas",size=8)
    plt.title("Dirección del viento")
    ax.get_yaxis().set_visible(False)
    i=0

    print(".----------------------------------------.....")
    while i< len(x):
        print(x[i])
        print(a[i])
        ax.quiver(x[i],0,a[i],-100 ,color= colors(t[i]) )
        i=i+1

    if(aux==0):
        plt.savefig("WindDirection.png",bbox_inches="tight")
    
    else:
        plt.savefig("WindDirection2.png",bbox_inches="tight")



#Función que crea una gráfica con los datos de dirección de oleaje y lo guarda en una imagen.
#Ah esta función se le pasan tres argumentos:
#   -grados: vector con la direccion de oleaje para las horas establecidas
#   -aux: variable auxiliar que indica si la grafica es para el dia actual o para 
#   -tem: vector con la temperatura del agua para las horas establecidas
def grafica2(grados,aux,tem):
    print(tem)
    if(len(grados)==13):
        x= np.linspace(0,24,13)
        ejex=["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00","00:00"]
   
    else:
        x = np.linspace(1, 23, 12)
        ejex=["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00"]
   

    fig = plt.figure()
    fig.set_size_inches(8,2)
    ax = fig.gca()
    #print(np.zeros(x.shape))

    t=[]
    characters=" ºC"
    i=0
    for z in tem:
      t.append(''.join(y for y in z if y not in characters))
      t[i]=float(t[i])
      i=i+1


    a=[]
    i=0
    #print("--------------------------------------------")
    #print(grados)
    #print(x)
    while(i<len(grados)):
        b=-np.tan(grados[i])*x[i]
        a.append(1-b)
        i=i+1;
   
    plt.xticks(x,ejex)
    plt.xlabel("horas",size=8)
    plt.title("Dirección de oleaje")
    ax.get_yaxis().set_visible(False)
    i=0
    while i< len(x):
        ax.quiver(x[i],0,a[i],-100,color=colors(t[i]) )
        i=i+1

    if(aux==0):
        plt.savefig("SwellDirection.png",bbox_inches="tight")
    else:
         plt.savefig("SwellDirection2.png",bbox_inches="tight")


def guia():
    
    i=0
    l=["<=0ºC","0ºC>y<=5ºC","5ºC>y<=10ºC","10ºC>y<=15ºC","15ºC>y<=20ºC","20ºC>y<=25ºC","25ºC>y<=30ºC","30ºC>y<=35ºC","35ºC>y<=40ºC"
        ,"40ºC>y<=45ºC",">45ºC"]

    plt.figure(figsize=(2.5,3))
    plt.axhline(y=2, xmin=0.1, xmax=0.3, color="royalblue")
    plt.axhline(y=3, xmin=0.1, xmax=0.3, color="turquoise")
    plt.axhline(y=4, xmin=0.1, xmax=0.3, color="mediumspringgreen")
    plt.axhline(y=5, xmin=0.1, xmax=0.3, color="limegreen")
    plt.axhline(y=6, xmin=0.1, xmax=0.3, color="lightsalmon")
    plt.axhline(y=7, xmin=0.1, xmax=0.3, color="salmon")
    plt.axhline(y=8, xmin=0.1, xmax=0.3, color="orange")
    plt.axhline(y=9, xmin=0.1, xmax=0.3, color="orangered")
    plt.axhline(y=10, xmin=0.1, xmax=0.3, color="firebrick")
    plt.axhline(y=11, xmin=0.1, xmax=0.3, color="red")
    plt.axhline(y=12, xmin=0.1, xmax=0.3, color="darkred")

    n=2
    i=0
    while i<len(l):
        plt.text(0.6,n,l[i], ha="center", size="x-small")
        n=n+1
        i=i+1

    plt.axis('off')
    #plt.show()
    plt.savefig("guia.png",bbox_inches="tight")
