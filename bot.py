#Libreria para conectarse con el bot de telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler

import time
import schedule

#Para los hilos
import threading

#Para enviar mensajes sin otro mensaje previo 
import telepot


#Clase Forecast y BBDD
import Forecast
import BBDD


import os
import json

#Token del bot de telegram
BOT_TOKEN = '5257201108:AAFkh9t-lYtHy2zThEvMVMst-eqwOC_jgM0'




#Variables globales de apoyo
GLOBAL=0
RESULT=""
GLOBALE=0
RESULTE=""
ID=""
USER=""



#Comando start para enviar un mensaje de bienvenida  
def start(update, context):  
    update.message.reply_text('Bienvenido, escribe /help')


#Comando help para enviar un mensaje con instrucciones
def help(update, context):
    update.message.reply_text('Los comandos son:\n')
    update.message.reply_text('/playa <nombre de la playa> : para suscribirse a una playa\n')
    update.message.reply_text('/Subs : para ver las playas a las que estas suscrito\n')
    update.message.reply_text('/Eliminar : Te muestra las playas que estas suscrito para eliminarla\n')


#Comando echo si se introduce un mal comando 
def echo(update, context):  
    update.message.reply_text('Comando mal introducido')



#Busqueda de la playa en la Base de Datos
def buscar(update,playa):


  
    n = playa[1:]
    result,count = BBDD.buscar(n)
    print(result)

    if(count == 0):
        update.message.reply_text('No se ha encontrado esa playa prueba otra vez ')
        return 0,0

    if (count == 1):
        for row in result:
            #print(row)
            CX = row['Coordenada_X']
            CY = row['Coordenada_Y']
            ZS = row['Zona_Surf']
            PR = row['Provincia']
            TN = row['Nombre']
            print("Playa= " +TN + "Provincia= "+PR+",Coordenada x="+ CX +", Coordenada y="+ CY + ", ZonaSurf="+ZS)
            return CX,CY

    print(count)
    print(result)
    
    t=0
    if (count > 1):
        update.message.reply_text('Elige una de la opciones : ')
        for row in result:
            #print(row)
            CX = row['Coordenada_X']
            CY = row['Coordenada_Y']
            ZS = row['Zona_Surf']
            PR = row['Provincia']
            TM = row['Termino_Municipal']
            TN= row['Nombre']
            update.message.reply_text("Playa= " +TN + " ,Provincia= "+PR+",Municipio="+TM+", ZonaSurf="+ ZS + " /"+str(t) )
            t=t+1

        global GLOBAL
        GLOBAL= t-1
        print("GLOBAL "+ str(GLOBAL))
        global RESULT
        RESULT=result
        return 0,0      
        
        


#Busqueda de la playa despues de haber escogido una opción.
#Solo se accede a este metodo si se hay varias opciones
def buscar2(update,playa):
    count=1
    print(playa)
    if (count == 1):  
        #print(row)
        CX = playa['Coordenada_X']
        CY = playa['Coordenada_Y']
        ZS = playa['Zona_Surf']
        PR = playa['Provincia']
        TM = playa['Termino_Municipal']
        TN = playa['Nombre']
        print("Playa: "+ TN + "Provincia= "+PR+",Coordenada x="+ CX +", Coordenada y="+ CY + ", ZonaSurf="+ZS)
        return CX,CY



#Comando playa para inscribirse a la playa que solicite el usuario
def suscripcion(update, context):
    global GLOBAL
    print("GLOBAL2 "+ str(GLOBAL))
    g = GLOBAL

    #Solo se entra aqui si ya se ha introducido el nombre de una playa y hay varias opciones
    if(g != 0):  
        print("ENTRA")
        print(update.message.text)
        s = update.message.text
        t = s.split('/')
        #Comprobación de que no se introduzca otra playa en vez de la opcion correcta
        if(len(t[1]) !=1):
            
            update.message.reply_text("Esa no es una opcion valida. Vuelve a introducir el nombre de la playa correcta")
            GLOBAL = 0
        else:
            #Comprobación de que la opcion que se ha introducida es una de las validas
            if(int(t[1]) > g):
                update.message.reply_text("Esa no es una opcion valida. Vuelve a introducir el nombre de la playa correcta")
                GLOBAL = 0
            else:
                GLOBAL = 0
                y,x = buscar2(update,RESULT[int(t[1]) ])
                if(y != x ):
                    aux=suscribirse(update, x,y)
                    if(aux==1):
                        x = str(x).replace(",",".")
                        y = str(y).replace(",",".")

                        print(x)
                        print(y)
                        update.message.reply_text("Te acabas de suscribir con exito")
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
            y,x = buscar(update,t[1])
            if(y != x ):    
                #update.message.reply_text("Coordenadas X: " + x + "Coordendas Y: " + y)
                
                
                aux=suscribirse(update, x,y)
                if(aux==1):
                    x = str(x).replace(",",".")
                    y = str(y).replace(",",".")

                    print(x)
                    print(y)
                    update.message.reply_text("Te acabas de suscribir con exito")
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
    
    nombre = row['Nombre']
    provincia = row['Provincia']
    municipio = row['Termino_Municipal']
    chat_id = update.message.chat_id
    user_first_name = str(update.message.chat.username)
    print(chat_id)
    print(user_first_name) 


    count,result=BBDD.buscarNomMun(chat_id, user_first_name)
    t=0
    for row in result:
        n = row['Nombre']
        p = row['Municipio']
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
            update.message.reply_text("Playa: "+ row['Nombre'] +" de "+ row['Municipio'] + " en " + row['Provincia'] + "\n")


#Comando eliminar el cual borra la playa que solicite el usuario de las que esta suscrito
def Unfollow(update, context):
    global GLOBALE
    global RESULTE
    chat_id = update.message.chat_id
    user_first_name = str(update.message.chat.username)
    g = GLOBALE
    if(g!= 0):

        s = update.message.text
        print(len(s))
        t = s.split('/')    
        t = t[1].split('p')
        print("-ENTRA-")
        t=t[0]
        row = RESULTE[int(t)]
        
        #print(row)
        n = row['Nombre'] 
        m = row['Municipio'] 
        p = row['Provincia']
        cx = row['CX']
        cy = row['CY']


        BBDD.eliminar(chat_id, user_first_name, n, m, p, cx, cy)

        update.message.reply_text("Playa eliminada")
        GLOBALE=0
        RESULTE=""
    
    else:
        s = update.message.text
        print("-ENTRA2-")
        if(len(s) ==3 ):
            update.message.reply_text("Comando mal introducido")
        else:
            count,result= BBDD.buscarNomMun(chat_id, user_first_name)
            if(count==0):
                update.message.reply_text("No hay playas en la lista")
            else:
                #print(result)
                t=0
                for row in result:
                    update.message.reply_text("Playa: "+ row['Nombre'] +" de "+ row['Municipio'] + " en " + row['Provincia'] + " /"+str(t)+"p" + "\n")
                    t=t+1
                
                RESULTE = result
                GLOBALE = 1


#Comando automatico que muestra la información meteorologica para las playas suscritas  del usuario
def subs_auto():
    bot= telepot.Bot(BOT_TOKEN)


    count,result=BBDD.playas_subs()
    aux=0
    for row in result:
        print(row)
        nombre=row['Nombre']
        provincia=row['Provincia']
        x = str(row['CX']).replace(",",".")
        y = str(row['CY']).replace(",",".")

        #LLamo al forecast
        Forecast.busqueda(nombre,provincia,x,y,aux)
        aux=1


    count2,result2=BBDD.subs_auto()
    global ID,USER

    for x in result2:
        print(x["ID"])
        id=x["ID"]
        print(x["Usuario"])
        user=x["Usuario"]

        bot.sendMessage(chat_id=id,text="----Mensaje automatico----")
        bot.sendMessage(chat_id=id,text="Playas suscritas de "+ user+"\n")

        count,result=BBDD.buscarNomMun(id,user)
        print(result)
        aux=0
        for row in result:
            #print(row)
            t="Playa: "+ row['Nombre'] +" de "+ row['Municipio'] + " en " + row['Provincia'] + "\n"
                        
            x=row['CX']
            y=row['CY']
                    
            x = str(x).replace(",",".")
            y = str(y).replace(",",".")
            if(aux==1):
                time.sleep(10)
            bot.sendMessage(chat_id=id,text=t)

            s="JSON"+row['Nombre']+"_"+row['Provincia']+".json"
            
            if(os.path.exists(s)):
                file = open(s,"r")
                json1=json.load(file)
                s="hilo"+str(aux)

                Forecast.Forecast1(BOT_TOKEN,id,json1)



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
    
    query=update.callback_query
    print(query)
    id=query['message']['message_id']
    chat=query['message']['chat']['id']
    print(chat)
    print(id)
    Forecast.cambioGV(id,chat)
    print("BotonIF")

def prueba():
    
    x=0
    while(x<2):
        if(x==1):
            BBDD.vivo2()
            x=0
        time.sleep(70)
        x=x+1
    

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

    dp.add_handler(CallbackQueryHandler(pattern="BI",callback=BotonI,pass_update_queue =True))
    dp.add_handler(CallbackQueryHandler(pattern="BD",callback=BotonD,pass_update_queue =True))
    dp.add_handler(CallbackQueryHandler(pattern="BGI",callback=BotonGV,pass_update_queue =True))
    dp.add_handler(CallbackQueryHandler(pattern="BGV",callback=BotonGS,pass_update_queue =True))
    

    g = 10
    while(g >= 0):
        s=str(g)
        dp.add_handler(CommandHandler(s, suscripcion))
        g = g -1
    
    n = 40
    while(n >= 0):
        x=str(n)+"p"
        dp.add_handler(CommandHandler(x, Unfollow))
        n = n -1

    
    # De no ejecutarse ninguno de los anteriores asumimos que el usuario escribió algo y ejecutamos el método echo que nos va a permitir obtener los campos de las búsquedas del usuario
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.run_async(prueba)
    print("hola")
    updater.start_polling()
    
    updater.idle()
    
    
    
    
#Función que se queda esperando y solo llama a la función subs_auto
#a la hora establecida. Esta función va como un hilo paralelo al hilo
#main
def automatico():
    schedule.every().day.at("17:30").do(subs_auto)
    schedule.every().day.at("13:00").do(subs_auto)
    schedule.every(50).seconds.do(BBDD.vivo)
    while True:
        schedule.run_pending()
        
        time.sleep(1)


#Primera función que se inicia al ejecutar el programa la cual crea un hilo
#paralelo al main 
if __name__ == '__main__':
    
    t=threading.Thread(name="hilo automatico",target=automatico)
    t.start()

    main()

