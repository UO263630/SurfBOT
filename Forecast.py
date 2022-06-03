"""
-Clase: Forecast.py
-Descripción:
"""
#Librerias para conectarse con Telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import telegram

#Libreria para obtener fechas y horas y manipularlas
import arrow

#Libreraia para crear tablas de datos
from tabulate import tabulate

#lLibreria para hacer peticiones HTTP
import requests

#Conexión con la clase Graficas
import Graficas

#Libreria para la apertura de archivos
import os

#Librerai para tratar archivos json
import json
    
import bot
#Variables auxiliares globales
AP=0
AUX=0
DIC=[]
DIC2=[]
TOKEN=""
N=[
'2149585a-a7a2-11ec-9a99-0242ac130002-214958d2-a7a2-11ec-9a99-0242ac130002',
'a8351102-a7a1-11ec-b16d-0242ac130002-a8351170-a7a1-11ec-b16d-0242ac130002',
'e827db8c-a7a1-11ec-b16d-0242ac130002-e827dc22-a7a1-11ec-b16d-0242ac130002',
'0434d41e-716b-11ec-9e35-0242ac130002-0434d48c-716b-11ec-9e35-0242ac130002'
]


#Función que obtiene las predicciones meteorologicas para cada playa
#y las guarda en archivos json diferentes, si estos archivos ya existen
#se sobreescriben
def busqueda(x,y,aux):
        print()
        global AP,AUX,N
        s="JSON_"+str(x)+"_"+str(y)+"_"+".json"
        if(os.path.exists(s) == False):
            
            if(aux==0):
                AP=0
                AUX=0
            if(AP==10):
                AP=0
                AUX=AUX+1
            s="JSON_"+str(x)+"_"+str(y)+"_"+".json"
            s2="JSON_"+str(x)+"_"+str(y)+"_OLAS"+".json"
                
            print(s)
            file = open(s,"w")
            file2=open(s2,"w")
            # Primera hora del día
            start = arrow.now().floor('day')
            print(start)
            # Última hora del día
            end = start.shift(days=+2)
            print(end)
           
            response = requests.get(
            'https://api.stormglass.io/v2/weather/point',
            params={
                'lat': x,
                'lng': y,
                'params': ','.join(['airTemperature', 'windSpeed','waveHeight','waveDirection','swellPeriod','swellHeight','swellDirection','waterTemperature']),
                'start': start.to('UTC+2').timestamp(),  # Convert to UTC timestamp
                'end': end.to('UTC+2').timestamp()  # Convert to UTC timestamp
            },
            headers={
                'Authorization': N[AUX].rstrip()
            }
            )

            response2 = requests.get(
            'https://api.stormglass.io/v2/tide/extremes/point',
            params={
                'lat': x,
                'lng': y,
                
                'start': start.to('UTC+2').timestamp(),  # Convert to UTC timestamp
                'end': end.to('UTC+2').timestamp(),  # Convert to UTC timestam
            },
            headers={
                'Authorization': N[AUX].rstrip()
            }
            )

            AP=AP+1
            print(AP)

            json_data = response.json()
            json_data2= response2.json()
            print("JSON")
            print(json_data2)

            json.dump(json_data , file)
            json.dump(json_data2,file2)
            file.close()
            file2.close()
            print("------------------------forecast---------------------")


#Función que se llama cada vez que se pulsa un boton. Su funcionamiento
#es el de cambiar los datos que se van a mostrar en función del boton
#que se ha pulsado y cambiar el boton que se tiene que mostrar. Esta
#función retorna el resultado de llamar a la función tablas
def datos(id,chat,b):
    tipo=9
    json=[]
    global DIC,DIC2
    print(id)
    print(chat)
    aux=0
    previa=0
    for x in DIC:
        d=[x[0],0]
        for n in DIC2:
            if(n[0]==x[0]):
                previa=1
        if(previa==0):
            DIC2.append(d)
    for x in DIC:
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,INICIO,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        print(x[0])
        print(x[3])
        if(x[0] ==id):
            #print(x[1])
            print(x[2])
            print(x[3])
            if(str(x[3]) == str(chat)):
                if(x[2]<=3 and aux==0):
                    x[2]=x[2]+4
                    tipo=x[2]
                    json=x[1]
                    aux=1
                    print(x[2])
                if(x[2]>=4 and x[2]<=7 and aux==0):
                    if(x[2]==4 or x[2]==6):
                        z=0
                        print(DIC2)
                        for r in DIC2:
                            if(r[0]==id):
                                z=r[1]
                                
                        if(z==0):
                            if(b==0):
                                x[2]=x[2]-4
                                tipo=x[2]
                                json=x[1]
                                aux=1
                                for r in DIC2:
                                    if(r[0]==id):
                                        r[1]=0

                                print(x[2])
                            else:
                                x[2]=x[2]+4
                                tipo=x[2]
                                json=x[1]
                                aux=1
                                for r in DIC2:
                                    if(r[0]==id):
                                        r[1]=1

                                print(x[2])
                        else:
                            if(b==0):
                                x[2]=x[2]-4
                                tipo=x[2]
                                json=x[1]
                                aux=1
                                print(x[2])
                            else:
                                x[2]=x[2]+4
                                tipo=x[2]
                                json=x[1]
                                aux=1
                                print(x[2])
                    else:
                        x[2]=x[2]-4
                        tipo=x[2]
                        json=x[1]
                        aux=1
                        print(x[2])
                if(x[2]>=8 and aux==0):           
                    x[2]=x[2]-4
                    tipo=x[2]
                    json=x[1]
                    aux=1
                    print(x[2])
                
                print(tipo)
                tabla=tablas(tipo,json)
                print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,FIN,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
                print(id)
                return tabla,tipo


#Función que obtiene los datos del json los ordena y devuelve la tabla
#o imagen necesaria en función del valor del parametro que se pasa como
#primer argumento
def tablas(id,json_data):
    
    # Primera hora del dia
    start = arrow.now().floor('day')
    print(start)
    # Ultima hora del dia
    end = start.shift(days=+2)
    print(end)

    data= []
    data2= []
    data3= []
    data4 = []
    dirs=[]
    dirv=[]
    dirs2=[]
    dirv2=[]
    tem1=[]
    tem2=[]
    tem3=[]
    tem4=[]
    x=1
    

    f=str(start).split("T")
    dia=f[0].split("-")
    for row in json_data['hours']:
        if(row['time'] >= str(start) and x%2!=0 ):
            dyh=row['time']
            fecha=dyh.split("T")
            di=fecha[0].split("-")
            if(fecha[0] == f[0] ):
                fecha=dyh.split("T")
                fecha=fecha[1].split("+")
                time = fecha[0].split(":")
                time=time[0]+":"+time[1]

                aT = str(row['airTemperature']['noaa'])
            
                n=aT.split(".")
                if(len(n[1]) ==1):
                    aT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    aT=" "+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    aT="0"+n[0]+"."+n[1]+"0"

                aT=aT + " ºC"


                wS=str(row['windSpeed']['noaa'])
                wS=float(wS)
                wS=wS*3.6
                wS=round(wS, 2)
                wS=str(wS)
                w=wS.split(".")
                if(len(w[0])==1):
                    wS="0"+w[0]+"."+w[1]
                if(len(w[1])==1):
                    wS=w[0]+"."+w[1]+"0"
                if(len(w[0]) ==1 and len(w[1]) ==1):
                    wS="0"+w[0]+"."+w[1]+"0"
                wS=wS+ " km/h"

                wD=row['waveDirection']['noaa']

                sP=str(row['swellPeriod']['noaa'])

                n=sP.split(".")
                if(len(n[1]) ==1):
                    sP=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    sP="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    sP="0"+n[0]+"."+n[1]+"0"

                sP=sP + " s"
    
                sH=str(row['waveHeight']['noaa'])

                w=sH.split(".")
                if(len(w[1])==1):
                    sH=w[0]+"."+w[1]+"0"
                sH=sH + " m"

                sD=row['swellDirection']['noaa'] 
                
                wT=str(row['waterTemperature']['noaa'])

                n=wT.split(".")
                if(len(n[1]) ==1):
                    wT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    wT="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    wT="0"+n[0]+"."+n[1]+"0"

                wT=wT + " ºC"

                d= [ time , aT ,  wS ]
                d2= [time, sP,sH]
                data.append(d[:])
                data2.append(d2[:])
                dirv.append(wD)
                dirs.append(sD)
                tem1.append(aT)
                tem3.append(wT)
            if(int(di[2]) > int(dia[2]) or int(di[1]) > int(dia[1]) ):
                
                fecha=dyh.split("T")
                fecha=fecha[1].split("+")
                time = fecha[0].split(":")
                time=time[0]+":"+time[1]

                aT = str(row['airTemperature']['noaa'])
                
                n=aT.split(".")
                if(len(n[1]) ==1):
                    aT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    aT=" "+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    aT="0"+n[0]+"."+n[1]+"0"

                aT=aT + " ºC"


                wS=str(row['windSpeed']['noaa'])
                wS=float(wS)
                wS=wS*3.6
                wS=round(wS, 2)
                wS=str(wS)
                w=wS.split(".")
                if(len(w[0])==1):
                    wS="0"+w[0]+"."+w[1]
                if(len(w[1])==1):
                    wS=w[0]+"."+w[1]+"0"
                if(len(w[0]) ==1 and len(w[1]) ==1):
                    wS="0"+w[0]+"."+w[1]+"0"
                wS=wS+ " km/h"

                wD=row['waveDirection']['noaa']

                sP=str(row['swellPeriod']['noaa'])

                n=sP.split(".")
                if(len(n[1]) ==1):
                    sP=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    sP="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    sP="0"+n[0]+"."+n[1]+"0"

                sP=sP + " s"

                sH=str(row['waveHeight']['noaa']) 

                w=sH.split(".")
                if(len(w[1])==1):
                    sH=w[0]+"."+w[1]+"0"
                sH=sH + " m"

                sD=row['swellDirection']['noaa'] 

                wT=str(row['waterTemperature']['noaa'])

                n=wT.split(".")
                if(len(n[1]) ==1):
                    wT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    wT="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    wT="0"+n[0]+"."+n[1]+"0"

                wT=wT + " ºC"

                d= [time, aT, wS]
                d2= [time, sP, sH]
                data3.append(d[:])
                data4.append(d2[:])
                dirs2.append(sD)
                dirv2.append(wD)
                tem2.append(aT)
                tem4.append(wT)
        x=x+1


    if(id==0):
        tabla1=tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  )
        return tabla1
    if(id==1):
        Graficas.graficaViento(dirs,0,tem1,data)
        g="WindDirection.png"
        return g
    if(id==2):
        tabla3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  )
        return tabla3
    if(id==3):
        Graficas.graficaViento(dirs2,1,tem2,data3)
        g="WindDirection2.png"
        return g
    if(id==4):
        tabla2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) 
        return tabla2
    if(id==5):
        Graficas.graficaOleaje(dirv,0,tem3,data2)
        g="SwellDirection.png"
        return g
    if(id==6):
        tabla4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola"]  )
        return tabla4
    if(id==7):
        Graficas.graficaOleaje(dirv2,1,tem4,data4)
        g="SwellDirection2.png"
        return g
    if(id==8):
        d=[]
        for r in tem3:
            n=[r]
            d.append(n)
        tabla2= tabulate( d , headers=["Temperatura del agua"]  )
        return tabla2
    if(id==10):
        d=[]
        for r in tem4:
            n=[r]
            d.append(n)
        tabla2= tabulate( d , headers=["Temperatura del agua"]  ) 
        return tabla2
        
    print()


#Función que obtiene los datos del json y los ordena y devuelve las tablas
#e imagenes necesarias para que el bot muestre al usuario. A diferencia de
#la clase anterior esta solo se llama la primera vez que se muestran la
#información de cada playa
def Forecast1(BOT_TOKEN,chat_id,json_data,json_data2):
    print("<<<<<<<<<<<<<<<<<<<<<<<")

    global TOKEN,DIC
    TOKEN=BOT_TOKEN
    chat=chat_id


    
    # Primera hora del dia
    start = arrow.now().floor('day')
    print(start)
    # Ultima hora del dia
    end = start.shift(days=+2)
    print(end)

    x=1
    data= []
    data2= []
    data3= []
    data4 = []
    dirs=[]
    dirv=[]
    dirs2=[]
    dirv2=[]
    tem1=[]
    tem2=[]
    tem3=[]
    tem4=[]
    f=str(start).split("T")
    dia=f[0].split("-")
    
    wd = []
    print(json_data)
    for row in json_data['hours']:
        if(row['time'] >= str(start) and x%2!=0 ):
            dyh=row['time']
            fecha=dyh.split("T")
            di=fecha[0].split("-")
            if(fecha[0] == f[0] ):
                fecha=dyh.split("T")
                fecha=fecha[1].split("+")
                time = fecha[0].split(":")
                time=time[0]+":"+time[1]

                aT = str(row['airTemperature']['noaa'])
                
                n=aT.split(".")
                if(len(n[1]) ==1):
                    aT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    aT="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    aT="0"+n[0]+"."+n[1]+"0"

                aT=aT + " ºC"
                

                wS=str(row['windSpeed']['noaa'])
                wS=float(wS)
                wS=wS*3.6
                wS=round(wS, 2)
                wS=str(wS)
                w=wS.split(".")
                if(len(w[0])==1):
                    wS="0"+w[0]+"."+w[1]
                if(len(w[1])==1):
                    wS=w[0]+"."+w[1]+"0"
                if(len(w[0]) ==1 and len(w[1]) ==1):
                    wS="0"+w[0]+"."+w[1]+"0"
                wS=wS+ " km/h"

                wD=row['waveDirection']['noaa']

                sP=str(row['swellPeriod']['noaa'])

                n=sP.split(".")
                if(len(n[1]) ==1):
                    sP=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    sP="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    sP="0"+n[0]+"."+n[1]+"0"

                sP=sP + " s"

                sH=str(row['waveHeight']['noaa'])

                w=sH.split(".")
                if(len(w[1])==1):
                    sH=w[0]+"."+w[1]+"0"
                sH=sH + " m"

                sD=row['swellDirection']['noaa'] 
                
                wT=str(row['waterTemperature']['noaa'])

                n=wT.split(".")
                if(len(n[1]) ==1):
                    wT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    wT="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    wT="0"+n[0]+"."+n[1]+"0"

                wT=wT + " ºC"

                d= [time ,aT ,wS ]
                d2= [time, sP ,sH]
                data.append(d[:])
                data2.append(d2[:])
                dirv.append(wD)
                dirs.append(sD)
                tem1.append(aT)
                tem3.append(wT)
            if(int(di[2]) > int(dia[2]) or int(di[1]) > int(dia[1]) ):
                
                fecha=dyh.split("T")
                fecha=fecha[1].split("+")
                time = fecha[0].split(":")
                time=time[0]+":"+time[1]

                aT = str(row['airTemperature']['noaa'])

                n=aT.split(".")
                if(len(n[1]) ==1):
                    aT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    aT="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    aT="0"+n[0]+"."+n[1]+"0"

                aT=aT + " ºC"
                

                wS=str(row['windSpeed']['noaa'])
                wS=float(wS)
                wS=wS*3.6
                wS=round(wS, 2)
                wS=str(wS)
                w=wS.split(".")
                if(len(w[0])==1):
                    wS="0"+w[0]+"."+w[1]
                if(len(w[1])==1):
                    wS=w[0]+"."+w[1]+"0"
                if(len(w[0]) ==1 and len(w[1]) ==1):
                    wS="0"+w[0]+"."+w[1]+"0"
                wS=wS+ " km/h"

                wD=row['waveDirection']['noaa']

                sP=str(row['swellPeriod']['noaa'])

                n=sP.split(".")
                if(len(n[1]) ==1):
                    sP=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    sP="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    sP="0"+n[0]+"."+n[1]+"0"

                sP=sP + " s"

                sH=str(row['waveHeight']['noaa'])

                w=sH.split(".")
                if(len(w[1])==1):
                    sH=w[0]+"."+w[1]+"0"
                sH=sH + " m"

                sD=row['swellDirection']['noaa'] 

                wT=str(row['waterTemperature']['noaa'])

                n=wT.split(".")
                if(len(n[1]) ==1):
                    wT=n[0]+"."+n[1]+"0"
                if(len(n[0]) ==1):
                    wT="0"+n[0]+"."+n[1]
                if(len(n[0]) ==1 and len(n[1]) ==1):
                    wT="0"+n[0]+"."+n[1]+"0"

                wT=wT + " ºC"

                d= [ time , aT ,  wS ]
                d2= [time, sP,sH]
                data3.append(d[:])
                data4.append(d2[:])
                dirs2.append(sD)
                dirv2.append(wD)
                tem2.append(aT)
                tem4.append(wT)

        x=x+1
        
    pl=[]
    bj=[]
    pl2=[]
    bj2=[]
    for row in json_data2['data']:
        if(row['type']=='high'):
            p=row['time'].split("T")
            if(p[0]==f[0]):
                p=p[1].split("+")
                p=p[0].split(":")
                n=p[0]+":"+p[1]
                pl.append(n)
            else:
                p=p[1].split("+")
                p=p[0].split(":")
                n=p[0]+":"+p[1]
                pl2.append(n)
        else:
            p=row['time'].split("T")
            if(p[0]==f[0]):
                p=p[1].split("+")
                p=p[0].split(":")
                n=p[0]+":"+p[1]
                bj.append(n)
            else:
                p=row['time'].split("T")
                p=p[1].split("+")
                p=p[0].split(":")
                n=p[0]+":"+p[1]
                bj2.append(n)

    bot= telegram.Bot(BOT_TOKEN)
    



    tabla1=tabulate( data , headers=["hora","Temperatura" , "Velocidad viento"]  ) 
    
    
    tabla2= tabulate( data2 , headers=["hora","Periodo oleaje" , "Altura de ola"]  ) 
    
    
    partes = str(start).split("T")[0].split("-")

    convertida = "/".join(reversed(partes))
    aux=0
    te="Fecha:"+ convertida+"\n"+"Pleamar: "
    for row in pl:
        if(aux==0):
            te=te+row
        else:
            te=te+" ,"+row
        aux=1
    aux=0
    te=te+"\n"+"Bajamar: "
    for row in bj:
        if(aux==0):
            te=te+row
        else:
            te=te+" ,"+row
        aux=1


    bot.sendMessage(chat,text=te)
    f=bot.sendMessage( chat, tabla1,           
                    reply_markup=InlineKeyboardMarkup([
                        [buttonI]])
                    )

    msn=f['message_id']
    d=[msn,json_data,0,chat_id]
    DIC.append(d)
    print("-----MSN-----")
    print(msn)
    
    print(data)
    Graficas.graficaViento(dirs,0,tem1,data)

    Graficas.graficaOleaje(dirv,0,tem3,data2)


    n=bot.sendPhoto(chat_id=chat,
        photo=open('WindDirection.png','rb') ,
        reply_markup=InlineKeyboardMarkup([
                        [buttonGV]])
                    
    )
    print("----message_id------")
    print(n['message_id'])
    
    
    d=[n['message_id'],json_data,1,chat_id]

    DIC.append(d)

    f=start.shift(days=+1)
    partes = str(f).split("T")[0].split("-")
    #print(partes)
    aux=0
    convertida = "/".join(reversed(partes))
    te2="Dia siguiente:"+ convertida+"\n"+"Pleamar: "
    for row in pl2:
        if(aux==0):
            te2=te2+row
        else:
            te2=te2+" ,"+row
        aux=1
    aux=0
    te2=te2+"\n"+"Bajamar: "
    for row in bj2:
        if(aux==0):
            te2=te2+row
        else:
            te2=te2+" ,"+row
        aux=1

    bot.sendMessage(chat,text=te2)


    tabla3=tabulate( data3 , headers=["hora","Temperatura" , "Velocidad viento"]  ) 

    tabla4=tabulate( data4 , headers=["hora","Periodo oleaje" , "Altura de ola"]  )

    
    n=bot.sendMessage( chat, tabla3 ,           
                    reply_markup=InlineKeyboardMarkup([
                        [buttonI]])
                    )
    d=[n['message_id'],json_data,2,chat_id]

    DIC.append(d)
    

    Graficas.graficaViento(dirs2,1,tem2,data3)

    Graficas.graficaOleaje(dirv2,1,tem4,data4)

 
    n=bot.sendPhoto(chat_id=chat,
        photo=open('WindDirection2.png','rb'),
        reply_markup=InlineKeyboardMarkup([
                        [buttonGV]])
    )
    
    d=[n['message_id'],json_data,3,chat_id]

    DIC.append(d)
    

#Botones utilizados en los diferentes mensajes
buttonI = InlineKeyboardButton(
        text= "Mas Datos",
        callback_data='BD'
)
buttonD = InlineKeyboardButton(
        text= "Volver",
        callback_data='BI'
)
buttonGV = InlineKeyboardButton(
        text= "Mas Graficas",
        callback_data='BGV'
)
buttonGS = InlineKeyboardButton(
        text= "Grafica anterior",
        callback_data='BGI'
)


#Funciones realizan el cambio de información que se muestra en el mensaje
#en el que se pulsa el boton. La información que se muestra varia dependiendo
#del boton pulsado y del chat en el que esté.
def cambioI(id,chat):
    tabla,tipo=datos(id,chat,0)

    print(tipo)
    print("<<<<<<<<<<<<CAMBIOI_VOLVER<<<<<<<<<<<")
    bot2=telegram.Bot(TOKEN)
    if(tipo==0 or tipo==2):
        print("ENTRA2")
        bot2.editMessageText(text=tabla,
                    chat_id=chat,
                    message_id=id,
                    reply_markup=InlineKeyboardMarkup([
                    [buttonI]]
                    
                )
        )
    
    else:
        bot2.editMessageText(text=tabla,
                    chat_id=chat,
                    message_id=id,
                    reply_markup=InlineKeyboardMarkup([
                    [buttonD,buttonI]]
                    
                )
        )

def cambioD(id,chat):
    tabla,tipo=datos(id,chat,1)
    print(tipo)
    
    print("<<<<<<<<<<CAMBIOD<<<<<<<<<<<<<")
    bot2=telegram.Bot(TOKEN)
    if(tipo==8 or tipo==10):
        print("ENTRA1")
        bot2.editMessageText(text=tabla,
                        chat_id=chat,
                        message_id=id,
                        reply_markup=InlineKeyboardMarkup([
                        [buttonD]]
                        
                    )
        )
    else:
        bot2.editMessageText(text=tabla,
                        chat_id=chat,
                        message_id=id,
                        reply_markup=InlineKeyboardMarkup([
                        [buttonD,buttonI]]
                        
                    )
        )

def cambioGI(id,chat):
    tabla,tipo=datos(id,chat,2)
    print("<<<<<<<<<CAMBIOGI<<<<<<<<<<<<<<")
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageMedia(
                            media=InputMediaPhoto(media = open(tabla,'rb')),
                            reply_markup= InlineKeyboardMarkup([
                            [buttonGV]
                            ]),
                            chat_id=chat,
                            message_id=id
        )

def cambioGV(id,chat):
    tabla,tipo=datos(id,chat,2)
    print("<<<<<<<<<<CAMBIOGV<<<<<<<<<<<<<")
    bot2=telegram.Bot(TOKEN)
    bot2.editMessageMedia(
                            media=InputMediaPhoto(media = open(tabla,'rb')),
                            reply_markup= InlineKeyboardMarkup([
                            [buttonGS]
                            ]),
                            chat_id=chat,
                            message_id=id
        )

def cambioGG(id,chat,token):
    print("<<<<<<<<<<CAMBIOGG<<<<<<<<<<<<<")
    bot2=telegram.Bot(token)
    Graficas.guia(1)
    bot2.editMessageMedia(
                            media=InputMediaPhoto(media = open("guia2.png",'rb')),
                            reply_markup= InlineKeyboardMarkup([
                            [bot.buttonG2]
                            ]),
                            chat_id=chat,
                            message_id=id
        )

def cambioGG2(id,chat,token):
    print("<<<<<<<<<<CAMBIOGG2<<<<<<<<<<<<<")
    bot2=telegram.Bot(token)
    Graficas.guia(0)
    bot2.editMessageMedia(
                            media=InputMediaPhoto(media = open("guia.png",'rb')),
                            reply_markup= InlineKeyboardMarkup([
                            [bot.buttonG]
                            ]),
                            chat_id=chat,
                            message_id=id
        )