#Libreria para funciones matematicas de alto nivel
import numpy as np

#Libreria para el diseño de gráficas
import matplotlib.pyplot as plt


#Función que va recibiendo la velocidad del viento para cada valor de la gráfica
#y en función de este le otorga un color determinado
def colors(t):
    #print(t)
    if(t>=0 and t<0.555556):
        return 'royalblue'
    if(t>=0.555556 and t<=1.66667):
        return 'turquoise'
    if(t>1.66667 and t<=3.33333):
        return 'mediumspringgreen'
    if(t>3.33333 and t<=5.55556):
        return 'limegreen'
    if(t>5.55556 and t<=8.1):
        return 'lightsalmon'
    if(t>8.1 and t<=10.8333):
        return 'salmon'
    if(t>10.8333 and t<=13.8889):
        return 'orange'
    if(t>13.8889 and t<=17.2222):
        return 'orangered'
    if(t>17.2222 and t<=20.8333):
        return 'firebrick'
    if(t>20.8333 and t<=24.7222):
        return 'red'
    if(t>24.7222 and t<=28.6111):
        return 'firebrick'
    if(t>28.6111 and t<=32.7778):
        return 'red'
    else:
        return 'darkred'
    



def grafica1(grados,aux,tem,data):
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
    print(t)

    while(i<len(grados)):
        b=-np.tan(grados[i])*x[i]
        a.append(1-b)
        i=i+1;

    print(len(x))
    #print(a)
    plt.xticks(x,ejex)
    plt.xlabel("horas",size=8)
    plt.title("Dirección del viento")
    
    i=0

    d=[]
    for r in data:
        n=r[2].split(" m/s")
        d.append(float(n[0]))

    
    print(d)
    print(".----------------------------------------.....")
    while i< len(x):
        #print(x[i])
       #print(a[i])
        ax.quiver(x[i],22,a[i],-100 ,color= colors(d[i]))
        i=i+1

    y=[0,5,10,15,20,25,30,35,40,45]
    ejey=["0ºC","5ºC","10ºC","15ºC","20ºC","25ºC","30ºC","35ºC","40ºC","45ºC"]
    t=[]
    for row in tem:
        r=row.split(" ºC")
        t.append(float(r[0]))


    plt.plot(x,t,marker=".",color="black",linestyle='solid')
    print(t)
    plt.yticks(y,ejey)
    plt.ylabel("Temperatura(ºC)",size=8)




    plt.show()


grados=[312.96, 311.4, 347.88, 62.41, 352.38, 317.23, 316.98, 316.99, 312.96, 304.9, 301.35, 299.53]
tem=['8.18 ºC', '7.46 ºC', '6.6 ºC', '5.58 ºC', '6.18 ºC', '8.4 ºC', '12.26 ºC', '12.42 ºC', '12.15 ºC', '11.45 ºC', '12.15 ºC', '11.45 ºC']
data=[['00:00', '06.63 ºC', '1.70 m/s'], ['02:00', '07.12 ºC', '1.76 m/s'], ['04:00', '07.25 ºC', '1.60 m/s'], ['06:00', '07.02 ºC', '1.23 m/s'], ['08:00', '10.65 ºC', '0.63 m/s'], ['10:00', '13.08 ºC', '0.98 m/s'], ['12:00', '14.32 ºC', '2.27 m/s'], ['14:00', '12.91 ºC', '2.05 m/s'], ['16:00', '11.78 ºC', '1.79 m/s'], ['18:00', '10.91 ºC', '1.49 m/s'], ['20:00', '09.41 ºC', '0.83 m/s'], ['22:00', '08.64 ºC', '0.80 m/s']]

grafica1(grados,0,tem,data)


