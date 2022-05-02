#Libreria para conectarse con el bot de telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import telegram
import time
import schedule

#Para los hilos
import threading

#Para enviar mensajes sin otro mensaje previo 
import telepot


#Clase Forecast y BBDD
import Forecast
import BBDD
import Graficas

import os
import json

from datetime import datetime 

#Token del bot de telegram
BOT_TOKEN = '5257201108:AAFkh9t-lYtHy2zThEvMVMst-eqwOC_jgM0'




#Variables globales de apoyo
GLOBAL=0
RESULT=""
GLOBALE=0
RESULTE=""
ID=""
USER=""
INFOS=0
INFO=""
FECHA=""

#Comando start para enviar un mensaje de bienvenida  
def start(update, context):
    update.message.reply_text("Bienvenido, la función principal de est bot es el envio diario al usuario"+
                              " de la información meteorológica de las playas que este decida.\n"+
                              "Si quieres conocer los comandos de este bot escribe el comando /help")



#Comando help para enviar un mensaje con instrucciones
def help(update, context):
    update.message.reply_text("Los comandos del bot son:\n"
                             + "/playa <nombre de la playa> : para suscribirse a una playa (max 3 playas por usuario)\n"
                             + "/Subs : para ver las playas a las que estas suscrito\n"
                             + "/Eliminar : Te muestra las playas que estas suscrito para eliminarla\n"
                             + "/info: ver información sobre la playa que decidas de las que estes suscrito\n"
                             + "/guia : muestra una guia de los colores de las graficas.\n"
                             + "/prediccion : muestra una predicción de las playas suscritas.\n"
                             + "A las 10:00 y a las 18:00 recibira un mensaje automatico junto con las\n"
                             + "predicciones de las playas suscritas. El horario de estas predicciones\n"
                             + "esta establecido en UTC+2 (hora de verano en la peninsula iberica)")




#Comando echo si se introduce un mal comando 
def echo(update, context):  
    update.message.reply_text('Comando mal introducido')



#Busqueda de la playa en la Base de Datos
def buscar(update,playa,aux):

    if (aux==1):
        print(playa)
        print("-------f---------")
        #CX = playa['Coordenada_X']
        #CY = playa['Coordenada_Y']
        #ZS = playa['Zona_Surf']
        #PR = playa['Provincia']
        #TM = playa['Termino_Municipal']
        #TN = playa['Nombre']
        CX = playa[0]
        CY = playa[1]
        ZS = playa[2]
        PR = playa[3]
        TM = playa[4]
        TN = playa[5]
        print("Playa: "+ TN + "Provincia= "+PR+",Coordenada x="+ CX +", Coordenada y="+ CY + ", ZonaSurf="+ZS)
        return CX,CY
    

    else:
        n = playa[1:]
        result,count = BBDD.buscar(n)
        print(result)

        if(count == 0):
            update.message.reply_text('No se ha encontrado esa playa prueba otra vez ')
            return 0,0

        if (count == 1):
            for row in result:
                print(row)
                print("----------------")
                #CX = row['Coordenada_X']
                #CY = row['Coordenada_Y']
                #ZS = row['Zona_Surf']
                #PR = row['Provincia']
                #TN = row['Nombre']
                CX = row[0]
                CY = row[1]
                ZS = row[2]
                PR = row[3]
                TN = row[5]
                print("Playa= " +TN + "Provincia= "+PR+",Coordenada x="+ CX +", Coordenada y="+ CY + ", ZonaSurf="+ZS)
                return CX,CY

        print(count)
        print(result)
        
        t=0
        if (count > 1):
            update.message.reply_text('Elige una de la opciones : ')
            for row in result:
                print(row)
                print("-----------f2-----")
                #CX = row['Coordenada_X']
                #CY = row['Coordenada_Y']
                #ZS = row['Zona_Surf']
                #PR = row['Provincia']
                #TM = row['Termino_Municipal']
                #TN= row['Nombre']
                CX = row[0]
                CY = row[1]
                ZS = row[2]
                PR = row[3]
                TM = row[4]
                TN= row[5]
                update.message.reply_text("Playa= " +TN + " ,Provincia= "+PR+",Municipio="+TM+", ZonaSurf="+ ZS + " /"+str(t) )
                t=t+1

            global GLOBAL
            GLOBAL= t-1
            print("GLOBAL "+ str(GLOBAL))
            global RESULT
            RESULT=result
            return 0,0      



#Comando playa para inscribirse a la playa que solicite el usuario
def suscripcion(update, context):
    global GLOBAL,RESULT
    print("GLOBAL2 "+ str(GLOBAL))
    g = GLOBAL
    s = update.message.text
    t = s.split('/')
    print("-------------t------------")
    print(len(t[1]))
    print(g)
    #Solo se entra aqui si ya se ha introducido el nombre de una playa y hay varias opciones
    if((g != 0) and ( (len(t[1])==1) or (len(t[1])==2)  ) ):  
        print("ENTRA")
        print(update.message.text)
        s = update.message.text
        t = s.split('/')
        print(g)
        #Comprobación de que no se introduzca otra playa en vez de la opcion correcta
        if( (len(t[1])!=2) and (len(t[1])!=1) ):
            print("ENTRA2")
            print(t[1])
            print(g)
            update.message.reply_text("Esta no es una opcion valida. Vuelve a introducir el nombre de la playa correcta")
            GLOBAL = 0
        else:
            print("ENTRA3")
            print(t[1])
            print(g)
            #Comprobación de que la opcion que se ha introducida es una de las validas
            if(int(t[1]) > g):
                update.message.reply_text("Esa no es una opcion valida. Vuelve a introducir el nombre de la playa correcta")
                GLOBAL = 0
            else:
                GLOBAL = 0
                print(RESULT)
                y,x = buscar(update,RESULT[int(t[1])] , 1)
                if(y != x ):
                    aux=suscribirse(update, x,y)
                    if(aux==1):
                        x = str(x).replace(",",".")
                        y = str(y).replace(",",".")

                        print(x)
                        print(y)
                        update.message.reply_text("Te acabas de suscribir con exito.\n"+
                                              " Recibiras un mensaje automatico junto con la prediccion de la playa\n"+
                                              " a las 10 y a las 18")
                        #print("///////////////////////")


    else:
        print(update.message.text)
        s = update.message.text
        t = s.split('/')
        
        #Comprobación de que no se introduce un valor erroneo 
        x=0
        aux=g
        if(len(t[1]) <= 1 ):
            while(g >= 0):
                if(t[1] != g):
                    x=x+1
                g = g - 1
        
        t=s.split('/playa')
        print(t[1])
        if(x>0 or t[1] =="" ):
            update.message.reply_text("Esa no es una opcion valida. Vuelve a introducir el nombre de la playa correcta")
            GLOBAL = 0

        else:    
            t = s.split('/playa')
            print(t[1])
            update.message.reply_text('Playa: ' + t[1])
            y,x = buscar(update,t[1],0)
            if(y != x ):    
                #update.message.reply_text("Coordenadas X: " + x + "Coordendas Y: " + y)
                
                
                aux=suscribirse(update, x,y)
                if(aux==1):
                    x = str(x).replace(",",".")
                    y = str(y).replace(",",".")

                    print(x)
                    print(y)
                    update.message.reply_text("Te acabas de suscribir con exito.\n"+
                                              " Recibiras un mensaje automatico junto con la prediccion de la playa\n"+
                                              " a las 10 y a las 18")
                    #print("///////////////////////")           
                else:
                    print("")

    print("---------------------------------------------")



#Función que suscribe la playa seleccionada al usuario siempre que pueda
def suscribirse(update,x,y): 

    aux=0
    count,result = BBDD.buscarCoo(x,y)


    print(result)
    row = result[0]
    
    #nombre = row['Nombre']
    #provincia = row['Provincia']
    #municipio = row['Termino_Municipal']
    nombre = row[0]
    provincia = row[1]
    municipio = row[2]
    chat_id = update.message.chat_id
    user_first_name = str(update.message.chat.username)
    print(chat_id)
    print(user_first_name) 


    count,result=BBDD.buscarNomMun(chat_id, user_first_name)
    t=0
    for row in result:
        print(row)
        #n = row['Nombre']
        #p = row['Municipio']
        n = row[0]
        p = row[1]
        if(n == nombre and p == municipio):
            t= t +1;

    print(result)

    count,result=BBDD.buscarNomMun(chat_id, user_first_name)
    if(count>=3):
        update.message.reply_text("No puedes suscribirte a mas playas")
        
    else:
        if(t==0):
            BBDD.insertar(chat_id, user_first_name ,nombre, provincia, municipio, x,y)

            aux=1
        else:
            update.message.reply_text("Ya estas suscrito a esa playa")
    print(aux)
    return aux



#Comando subs que muestra las playas a las que esta suscrita el usuario
def subs(update, context):
     
    print("entra")
    chat_id = update.message.chat_id
    user_first_name = str(update.message.chat.username)
    count,result=BBDD.buscarNomMun(chat_id, user_first_name)
    print(len(result))
    if(len(result) ==0):
        update.message.reply_text("No estas suscrito a ninguna playa")
    else:
        for row in result:
            #update.message.reply_text("Playa: "+ row['Nombre'] +" de "+ row['Municipio'] + " en " + row['Provincia'] + "\n")
            update.message.reply_text("Playa: "+ row[0] +" de "+ row[1] + " en " + row[2] + "\n")



#Comando eliminar el cual borra la playa que solicite el usuario de las que esta suscrito
def Unfollow(update, context):
    global GLOBALE
    global RESULTE
    chat_id = update.message.chat_id
    user_first_name = str(update.message.chat.username)
    g = GLOBALE
    s = update.message.text
    print(s)
    print(g)
    if(g!= 0 and s!="/eliminar"):

        s = update.message.text
        print(len(s))
        t = s.split('/')    
        t = t[1].split('p')
        print("-ENTRA-")
        t=t[0]
        row = RESULTE[int(t)]
        
        
        print("-----------------------------------------")
        print(row)
        #n = row['Nombre'] 
        #m = row['Municipio'] 
        #p = row['Provincia']
        #cx = row['CX']
        #cy = row['CY']
        n = row[0] 
        m = row[1] 
        p = row[2]
        cx = row[3]
        cy = row[4]


        BBDD.eliminar(chat_id, user_first_name, n, m, p, cx, cy)

        update.message.reply_text("Playa eliminada")
        GLOBALE=0
        RESULTE=""
    
    else:
        s = update.message.text
        print("-ENTRA2-")
        if(len(s) == 3 ):
            update.message.reply_text("Comando mal introducido")
        else:
            count,result= BBDD.buscarNomMun(chat_id, user_first_name)
            if(count==0):
                update.message.reply_text("No hay playas en la lista")
            else:
                #print(result)
                t=0
                for row in result:
                    #update.message.reply_text("Playa: "+ row['Nombre'] +" de "+ row['Municipio'] + " en " + row['Provincia'] + " /"+str(t)+"p" + "\n")
                    update.message.reply_text("Playa: "+ row[0] +" de "+ row[1] + " en " + row[2] + " /"+str(t)+"p" + "\n")
                    t=t+1
                
                RESULTE = result
                GLOBALE = 1



#Comando automatico que muestra la información meteorologica para las playas suscritas  del usuario
def subs_auto():
    bot= telepot.Bot(BOT_TOKEN)
    global FECHA
    p=0
    f=datetime.today().strftime('%Y-%m-%d')
    if(FECHA!=f):
        count,result=BBDD.playas_subs()
        aux=0
        for row in result:
            print(row)

            x = str(row[3]).replace(",",".")
            y = str(row[4]).replace(",",".")
            s="JSON_"+str(x)+"_"+str(y)+"_"+".json"
            if(os.path.exists(s)):
                os.remove(s)
        p=1

    print(datetime.today().strftime('%Y-%m-%d'))
    FECHA=datetime.today().strftime('%Y-%m-%d')


    if(p==1):
        count,result=BBDD.playas_subs()
        aux=0
        for row in result:
            print(row)
            #nombre=row['Nombre']
            #provincia=row['Provincia']
            #x = str(row['CX']).replace(",",".")
            #y = str(row['CY']).replace(",",".")
            nombre=row[0]
            provincia=row[1]
            municipio=row[2]
            x = str(row[3]).replace(",",".")
            y = str(row[4]).replace(",",".")

            #Llamo al forecast
            Forecast.busqueda(x,y,aux)
            aux=1


    count2,result2=BBDD.subs_auto()
    global ID,USER

    for x in result2:
        #print(x)
        #print(x["ID"])
        #id=x["ID"]
        #print(x["Usuario"])
        #user=x["Usuario"]
        print(x[0])
        id=x[0]
        print(x[1])
        user=x[1]

        bot.sendMessage(chat_id=id,text="----Mensaje automatico----")
        bot.sendMessage(chat_id=id,text="Playas suscritas de "+ user+"\n")

        count,result=BBDD.buscarNomMun(id,user)
        print(result)
        aux=0
        for row in result:
            print(row)
            #t="Playa: "+ row['Nombre'] +" de "+ row['Municipio'] + " en " + row['Provincia'] + "\n"
            t="Playa: "+ row[0] +" de "+ row[1] + " en " + row[2] + "\n"

            x=row[3]
            y=row[4]
            #x=row['CX']
            #y=row['CY']
                    
            x = str(x).replace(",",".")
            y = str(y).replace(",",".")
            if(aux==1):
                time.sleep(10)
            bot.sendMessage(chat_id=id,text=t)

            #s="JSON"+row['Nombre']+"_"+row['Provincia']+".json"
            s="JSON_"+str(x)+"_"+str(y)+"_"+".json"
            s2="JSON_"+str(x)+"_"+str(y)+"_OLAS"+".json"

            if(os.path.exists(s)):
                file = open(s,"r")
                json1=json.load(file)
                #s="hilo"+str(aux)
                file2=open(s2,"r")
                json2=json.load(file2) 
                Forecast.Forecast1(BOT_TOKEN,id,json1,json2)
                file.close()
                file2.close()



            print("////////////////////")
                        

            aux=1







#Funciones que capturan cuando se pulsa un boton y manda la información para cambiar el mensaje indicado
def BotonI(update,context):
    print("----------------------------")
    
    query=update.callback_query
    print(query)
    id=query['message']['message_id']
    chat=query['message']['chat']['id']
    print(chat)
    print(id)
    Forecast.cambioI(id,chat)
    print("BotonIF")

def BotonD(update,context):
    print("----------------------------")
    
    query=update.callback_query
    print(query)
    id=query['message']['message_id']
    chat=query['message']['chat']['id']
    print(chat)
    print(id)
    Forecast.cambioD(id,chat)
    print("BotonIF")

def BotonGV(update,context):
    print("----------------------------")
    
    query=update.callback_query
    print(query)
    id=query['message']['message_id']
    chat=query['message']['chat']['id']
    print(chat)
    print(id)
    Forecast.cambioGI(id,chat)
    print("BotonIF")

def BotonGS(update,context):
    print("----------------------------")
    
    #query=update.callback_query.chat.id
    query=update.callback_query
    print(query)
    id=query['message']['message_id']
    chat=query['message']['chat']['id']
    print(chat)
    print(id)
    Forecast.cambioGV(id,chat)
    print("BotonIF")

def BotonGG(update,context):
    print("----------------------------")
    
    query=update.callback_query
    print(query)
    id=query['message']['message_id']
    chat=query['message']['chat']['id']
    print(chat)
    print(id)
    Forecast.cambioGG(id,chat,BOT_TOKEN)
    print("BotonGG")


def BotonGG2(update,context):
    print("----------------------------")
    
    query=update.callback_query
    print(query)
    id=query['message']['message_id']
    chat=query['message']['chat']['id']
    print(chat)
    print(id)
    Forecast.cambioGG2(id,chat,BOT_TOKEN)
    print("BotonGG2")

#COmando para la busqueda de información sobre las playas suscritas
def infoplaya(update,context):
    print(update.message.text)
    text=update.message.text
    global INFOS
    global INFO
    n = INFOS

    if( n!=0 and text!="/info"):
        
        n=text.split("/infoplaya")
        #print(n[1])
        t=n[1].split("p")
        #print(t[0]) 
        
        i=INFO[int(t[0])]
        print(i)

        x=i[3]
        y=i[4]
        result=BBDD.info_playa(x,y)
        
        #print(result[0])
        result=result[0]
        n=""
        if(result[34] !=""):
            n="( " + result[34] + " )"
        update.message.reply_text("Playa "+ result[5] + ": " + result[8] + " Con una longitud de " + str(result[9]) + " y " + str(result[10]) + " de anchura y " 
                                + "condiciones de agua: " +  result[17]+".\n"+
                                "Aparcamiento: " + result[32]+ n + "\n"+
                                "Aseos: " + result[35]+"\n"+
                                "Lavapies: " + result[36]+"\n"+
                                "Duchas: " + result[37] +"\n"+
                                "Zona Deportiva: "+ result[48] +"\n"+
                                "Zona de Surf: " + result[51] +"\n")



        INFOS=0
        INFO=""
        print("---FIN IF INFOPLAYA---")

    else:

        if(text != "/info"):
            INFOS=0
            INFO=""
            update.message.reply_text("Comando mal introducido")

        else:
            chat_id = update.message.chat_id
            user_first_name = str(update.message.chat.username)
            count,result=BBDD.buscarNomMun(chat_id, user_first_name)
            i=0
            if(len(result) ==0):
                update.message.reply_text("No estas suscrito a ninguna playa")
            else:
                
                for row in result:
                    s="/infoplaya"+str(i)+"p"
                    update.message.reply_text("Playa: "+ row[0] +" de "+ row[1] + " en " + row[2] + " " + s +"\n")
                    i=i+1
                
                INFOS=1
                INFO=result
        
        print("---FIN ELSE INFOPLAYA---")



buttonG = InlineKeyboardButton(
        text= "Guia grafica de oleajes",
        callback_data='BGG'
)

buttonG2 = InlineKeyboardButton(
        text= "Guia grafica de viento",
        callback_data='BG2'
)

def guiacolores(update,context):
    update.message.reply_text("Las diferentes gráficas que se muestran con las prediccciones "+
                               "meteorologicas van coloreadas en función de la temperatura del aire y del agua respectivamente.\n"+
                               "Estos colores y la relación con los grados centigrados son:")
    Graficas.guia(0)
    bot=telegram.Bot(BOT_TOKEN)
    f=bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open('guia.png','rb'),
        reply_markup=InlineKeyboardMarkup([
                        [buttonG]])
                    )


    
def prediccion(update,context):
    print("----------------------------")
    bot = telepot.Bot(BOT_TOKEN)
    p=0
    chat_id = update.message.chat_id
    user_first_name = str(update.message.chat.username)
    print(chat_id)
    print(user_first_name)
    count,result=BBDD.buscarNomMun(chat_id,user_first_name)
    print(count)
    print(result)

    global FECHA
 
    f=datetime.today().strftime('%Y-%m-%d')
    if(FECHA!=f):
        count2,result2=BBDD.playas_subs()
        aux=0
        for row2 in result2:
            print(row2)

            x = str(row2[3]).replace(",",".")
            y = str(row2[4]).replace(",",".")
            s="JSON_"+str(x)+"_"+str(y)+"_"+".json"
            if(os.path.exists(s)):
                os.remove(s)
        p=1

    print(datetime.today().strftime('%Y-%m-%d'))
    FECHA=datetime.today().strftime('%Y-%m-%d')


    if(count==0):
        update.message.reply_text("No esta suscrito a ninguna playa")
    else:
        if(p==1):
            print("____________ENTRA____________")
            print(result)
            aux=0
            for row in result:
                print(row)
                #nombre=row['Nombre']
                #provincia=row['Provincia']
                #x = str(row['CX']).replace(",",".")
                #y = str(row['CY']).replace(",",".")
                nombre=row[0]
                provincia=row[1]
                municipio=row[2]
                x = str(row[3]).replace(",",".")
                y = str(row[4]).replace(",",".")

                #Llamo al forecast
                Forecast.busqueda(x,y,aux)
                aux=1
        
        count2,result2=BBDD.playas_subs()
        for row2 in result2:
            x = str(row2[3]).replace(",",".")
            y = str(row2[4]).replace(",",".")
            s="JSON_"+str(x)+"_"+str(y)+"_"+".json"
            if(os.path.exists(s) ==False):
                print("____________ENTRA2____________")
                Forecast.busqueda(x,y,aux)


        bot.sendMessage(chat_id=chat_id,text="Playas suscritas de "+ user_first_name+"\n")

        aux=0
        for row in result:
            print(row)
            #t="Playa: "+ row['Nombre'] +" de "+ row['Municipio'] + " en " + row['Provincia'] + "\n"
            t="Playa: "+ row[0] +" de "+ row[1] + " en " + row[2] + "\n"

            x=row[3]
            y=row[4]
            #x=row['CX']
            #y=row['CY']
                    
            x = str(x).replace(",",".")
            y = str(y).replace(",",".")
            if(aux==1):
                time.sleep(10)
            bot.sendMessage(chat_id=chat_id,text=t)

            #s="JSON"+row['Nombre']+"_"+row['Provincia']+".json"
            s="JSON_"+str(x)+"_"+str(y)+"_"+".json"
            s2="JSON_"+str(x)+"_"+str(y)+"_OLAS"+".json"
            if(os.path.exists(s)):
                file = open(s,"r")
                json1=json.load(file)
                #s="hilo"+str(aux)
                file2=open(s2,"r")
                json2=json.load(file2)
                Forecast.Forecast1(BOT_TOKEN,chat_id,json1,json2)
                file.close()
                file2.close()

            print("DIC")
            print(Forecast.DIC)
            print("////////////////////")
                        

            aux=1


#Función main
def main():
    # Creamos el Updater y le pasamos el token de nuestro bot. Este se encargará de manejar las peticiones de los usuarios.
    updater = Updater(BOT_TOKEN)

    # Obtenemos el Dispatcher para crear los comandos
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start)) 
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("Subs", subs))
    dp.add_handler(CommandHandler("Eliminar", Unfollow))
    dp.add_handler(CommandHandler("playa", suscripcion))
    dp.add_handler(CommandHandler("info", infoplaya))
    dp.add_handler(CommandHandler("guia", guiacolores))
    dp.add_handler(CommandHandler("prediccion", prediccion))

    dp.add_handler(CallbackQueryHandler(pattern="BI",callback=BotonI,pass_update_queue =True))
    dp.add_handler(CallbackQueryHandler(pattern="BD",callback=BotonD,pass_update_queue =True))
    dp.add_handler(CallbackQueryHandler(pattern="BGI",callback=BotonGV,pass_update_queue =True))
    dp.add_handler(CallbackQueryHandler(pattern="BGV",callback=BotonGS,pass_update_queue =True))
    dp.add_handler(CallbackQueryHandler(pattern="BGG",callback=BotonGG,pass_update_queue =True))
    dp.add_handler(CallbackQueryHandler(pattern="BG2",callback=BotonGG2,pass_update_queue =True))
    

    g = 40
    while(g >= 0):
        s=str(g)
        dp.add_handler(CommandHandler(s, suscripcion))
        g = g -1
    
    n = 4
    while(n >= 0):
        x=str(n)+"p"
        dp.add_handler(CommandHandler(x, Unfollow))
        n = n -1

    
    i = 4
    while(i >= 0):
        x="infoplaya"+str(i)+"p"
        dp.add_handler(CommandHandler(x, infoplaya))
        i = i -1

    i = 4
    while(i >= 0):
        x="pred"+str(i)+"n"
        dp.add_handler(CommandHandler(x, infoplaya))
        i = i -1

    # De no ejecutarse ninguno de los anteriores asumimos que el usuario escribió algo y ejecutamos el método echo que nos va a permitir obtener los campos de las búsquedas del usuario
    dp.add_handler(MessageHandler(Filters.text, echo))

    print("hola")
    updater.start_polling()
    
    updater.idle()
    

    
    
#Función que se queda esperando y solo llama a la función subs_auto
#a la hora establecida. Esta función va como un hilo paralelo al hilo
#main
def automatico():
    schedule.every().day.at("08:00").do(subs_auto)  #10:00
    schedule.every().day.at("16:00").do(subs_auto)  #18:00

    #schedule.every().day.at("14:40").do(subs_auto)  #16:40

    while True:
        schedule.run_pending()
        
        time.sleep(1)


#Primera función que se inicia al ejecutar el programa la cual crea un hilo
#paralelo al main 
if __name__ == '__main__':
    
    t=threading.Thread(name="hilo automatico",target=automatico)
    t.start()

    main()

