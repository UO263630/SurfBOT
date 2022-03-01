import numpy as np

import matplotlib.pyplot as plt

def grafica1(grados,aux):

    x = np.linspace(1, 23, 12)
    #grados=[306.76, 306.55, 306.29, 306.45, 307.03, 320.28, 321.86, 311.77, 311.85, 310.8, 308.63, 310.16]
    ejex=["01:00","03:00","05:00","07:00","09:00","11:00","13:00","15:00","17:00","19:00","21:00","23:00"]
   

    fig = plt.figure()
    ax = fig.gca()
    #print(x)
    #print(np.zeros(x.shape))

    

    a=[]
    i=0
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
    while i< len(x):
        ax.quiver(x[i],0,a[i],-100)
        i=i+1

    if(aux==0):
        plt.savefig("WindDirection.png",bbox_inches="tight")
    
    else:
        plt.savefig("WindDirection2.png",bbox_inches="tight")
    #plt.show()
    


def grafica2(grados,aux):
    
    x = np.linspace(1, 23, 12)
    #grados=[306.76, 306.55, 306.29, 306.45, 307.03, 320.28, 321.86, 311.77, 311.85, 310.8, 308.63, 310.16]
    ejex=["01:00","03:00","05:00","07:00","09:00","11:00","13:00","15:00","17:00","19:00","21:00","23:00"]


    fig = plt.figure()
    ax = fig.gca()
    #print(x)
    #print(np.zeros(x.shape))

   

    a=[]
    i=0
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