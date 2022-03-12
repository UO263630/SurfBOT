import numpy as np

import matplotlib.pyplot as plt
import matplotlib


def colors(t):
    if(t<=0):
        return 'blue3'
    if(t>0 and t<=3):
        return 'royalblue'
    if(t>3 and t<=5):
        return 'mediumspringgreen'
    if(t>5 and t<=10):
        return 'limegreen'
    if(t>10 and t<=15):
        return 'orange'
    if(t>15 and t<=20):
        return 'orangered1'
    else:
        return 'orangered'



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

    characters=" m/s"
    i=0
    for z in tem:
      t.append(''.join(y for y in z if y not in characters))
      t[i]=float(t[i])
      i=i+1
      

    print(t)

    a=[]
    i=0
    #print("--------------------------------------------")
    #print(grados)
    #print(x)
    while(i<len(grados)):
        b=-np.tan(grados[i])*x[i]
        a.append(1-b)
        i=i+1;

    #print(len(a))
    #print(a)
    plt.xticks(x,ejex)
    plt.xlabel("horas",size=8)
    plt.title("Dirección del viento")
    ax.get_yaxis().set_visible(False)
    i=0

    norm = matplotlib.colors.Normalize()
    cm = matplotlib.cm.copper

    while i< len(x):
        
        ax.quiver(x[i],0,a[i],-100 ,color= colors(t[i]) )
        i=i+1

    if(aux==0):
        plt.savefig("WindDirection.png",bbox_inches="tight")
    
    else:
        plt.savefig("WindDirection2.png",bbox_inches="tight")
    #plt.show()




def grafica2(grados,aux,tem):
    
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
        ax.quiver(x[i],0,a[i],-100)
        i=i+1

    if(aux==0):
        plt.savefig("SwellDirection.png",bbox_inches="tight")
    else:
         plt.savefig("SwellDirection2.png",bbox_inches="tight")
    #plt.show()


#grafica1()
#grafica2()