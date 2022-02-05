#Libreria para conectarse con el bot de telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Libreria para el acceso a la base de datos
import pymysql


import getgfs


#Token del bot de telegram
BOT_TOKEN = '5257201108:AAFkh9t-lYtHy2zThEvMVMst-eqwOC_jgM0'




#Variables globales de apoyo
GLOBAL=0
RESULT=""
GLOBALE=0
RESULTE=""

#Base de Datos de playas
database_host = 'bnhukxmv5yeixvtezd51-mysql.services.clever-cloud.com' 
username = 'uhvo87uj6up0zzym' 
password = 'Qlh2E0viyQFPSEdQ6PHc' 
database_name = 'bnhukxmv5yeixvtezd51' 


db = pymysql.connect(host= database_host,
                            user=username,
                            password=password,
                            database=database_name,
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


# Configuramos el comando start para enviar un mensaje de bienvenida  
def start(update, context):  
    update.message.reply_text('Bienvenido, escribe /help')


# Configuramos el comando help para enviar un mensaje con instrucciones
def help(update, context):
    update.message.reply_text('Los comandos son:\n')
    update.message.reply_text('/playa <nombre de la playa> : para suscribirse a una playa\n')
    update.message.reply_text('/Subs : para ver las playas a las que estas suscrito\n')
    update.message.reply_text('/Eliminar : Te muestra las playas que estas suscrito para eliminarla\n')





#Busqueda de la playa en la Base de Datos
def buscar(update,playa):

    cursor = db.cursor()
    
    n = playa[1:]
    print(n)
    print(len(playa))
    print(len(n))

    count = cursor.execute("SELECT Coordenada_X,Coordenada_Y,Zona_Surf,Provincia,Termino_Municipal FROM BBDD WHERE Nombre = (%s) " ,n )


    result=cursor.fetchall()
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
            #print("Provincia= "+PR+",Coordenada x="+ CX +", Coordenada y="+ CY + ", ZonaSurf="+ZS)
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
            update.message.reply_text("Provincia= "+PR+",Municipio="+TM+", ZonaSurf="+ ZS + " /"+str(t) )
            t=t+1

        global GLOBAL
        GLOBAL= t-1
        print("GLOBAL "+ str(GLOBAL))
        global RESULT
        RESULT=result
        return 0,0      
        
        


    #db.close()

#Busqueda de la playa despues de haber esocogido una opción.
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
        #print("Provincia= "+PR+",Coordenada x="+ CX +", Coordenada y="+ CY + ", ZonaSurf="+ZS)
        return CX,CY




def echo(update, context):
    global GLOBAL
    #print("GLOBAL2 "+ str(GLOBAL))
    g = GLOBAL

    #Solo se entra aqui si ya se ha introducido el nombre de una playa y hay varias opciones
    if(g != 0):  
        #print("ENTRA")
        #print(update.message.text)
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
                    update.message.reply_text("Coordenadas X: " + x + "Coordendas Y: " + y)

                    suscribirse(update, x,y)
            

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
        if(x>0):
            update.message.reply_text("Esa no es una opcion valida. Vuelve a introducir el nombre de la playa correcta")
            GLOBAL = 0

        else:    
            t = s.split('/playa')
            print(t[1])
            update.message.reply_text('Playa: ' + t[1])
            y,x = buscar(update,t[1])
            if(y != x ):
                update.message.reply_text("Coordenadas X: " + x + "Coordenadas Y: " + y)

                suscribirse(update, x,y)
            
    print("---------------------------------------------")




def suscribirse(update,x,y): 
    cursor = db.cursor()
    
    count = cursor.execute("SELECT Nombre,Provincia,Termino_Municipal FROM BBDD WHERE Coordenada_Y = (%s) and Coordenada_X = (%s)" , (x , y ))
    
    print(count)

    result=cursor.fetchall()
    row = result[0]
    #print(row['Nombre'])
    nombre = row['Nombre']
    provincia = row['Provincia']
    municipio = row['Termino_Municipal']
    chat_id = update.message.chat_id
    user_first_name = str(update.message.chat.username)
    print(chat_id)
    print(user_first_name) 

    count = cursor.execute("SELECT Nombre,Municipio FROM suscrito WHERE ID = (%s) AND Usuario = (%s) ", (chat_id, user_first_name))
    result=cursor.fetchall()
    t=0
    for row in result:
        n = row['Nombre']
        p = row['Municipio']
        if(n == nombre and p == municipio):
            t= t +1;

    print(result)

    if(t==0):
        result=cursor.fetchall()
        
        count = cursor.execute("INSERT INTO suscrito (ID,Usuario,Nombre,Provincia,Municipio,CX,CY) VALUES (%s,%s,%s,%s,%s,%s,%s)", (chat_id, user_first_name ,nombre, provincia, municipio, x,y) )
        #count = cursor.execute("SELECT * FROM suscrito")
        #result=cursor.fetchall()
        #print(result)
        db.commit()
    else:
        update.message.reply_text("Ya estas suscrito a esa playa")
    


def subs(update, context):
     
    cursor = db.cursor()
    count = cursor.execute("SELECT * FROM suscrito")
    result= cursor.fetchall()
    print(result)
    for row in result:
        update.message.reply_text("Playa: "+ row['Nombre'] +" de "+ row['Municipio'] + " en " + row['Provincia'] + "\n")


def Unfollow(update, context):
    global GLOBALE
    global RESULTE
    cursor = db.cursor()
    #print("GLOBAL "+ str(GLOBALE))
    chat_id = update.message.chat_id
    user_first_name = str(update.message.chat.username)
    g = GLOBALE
    if(g!= 0):
        s = update.message.text
        print(len(s))
        t = s.split('/')
        t = t[1].split('p')
        #print(t[0])
        t=t[0]
        row = RESULTE[int(t)]
        #print(row)
        n = row['Nombre'] 
        m = row['Municipio'] 
        p = row['Provincia']
        cx = row['CX']
        cy = row['CY']
        count = cursor.execute("DELETE FROM suscrito WHERE ID = (%s) AND Usuario = (%s) AND Nombre = (%s) AND Municipio = (%s) AND Provincia = (%s) AND CX = (%s) AND CY = (%s)" , (chat_id, user_first_name, n, m, p, cx, cy  ))
        db.commit()
        #count = cursor.execute("SELECT * FROM suscrito")
        #result=cursor.fetchall()
        #print(result)
        update.message.reply_text("Playa eliminada")
        GLOBALE=0
        RESULTE=""
    
    else:
        s = update.message.text
        if(len(s) ==3 ):
            update.message.reply_text("Comando mal introducido")
        else:
            count = cursor.execute("SELECT * FROM suscrito WHERE ID = (%s) AND Usuario = (%s) " , (chat_id, user_first_name) )
            if(count==0):
                update.message.reply_text("No hay playas en la lista")
            else:
                result= cursor.fetchall()
                #print(result)
                t=0
                for row in result:
                    update.message.reply_text("Playa: "+ row['Nombre'] +" de "+ row['Municipio'] + " en " + row['Provincia'] + " /"+str(t)+"p" + "\n")
                    t=t+1
                
                RESULTE = result
                GLOBALE = 1







def main():
    # Creamos el Updater y le pasamos el token de nuestro bot. Este se encargará de manejar las peticiones de los usuarios.
    updater = Updater(BOT_TOKEN, use_context=True)

    # Obtenemos el Dispatcher para crear los comandos
    dp = updater.dispatcher

    # Creamos el comando /start y definimos que se ejecute este mismo método
    dp.add_handler(CommandHandler("start", start))
    # Creamos el comando /help y definimos que se ejecute el método help
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("playa", echo))
    dp.add_handler(CommandHandler("Subs", subs))
    dp.add_handler(CommandHandler("Eliminar", Unfollow))

    g = 10
    while(g >= 0):
        s=str(g)
        dp.add_handler(CommandHandler(s, echo))
        g = g -1
    
    n = 40
    while(n >= 0):
        x=str(n)+"p"
        dp.add_handler(CommandHandler(x, Unfollow))
        n = n -1


    # De no ejecutarse ninguno de los anteriores asumimos que el usuario escribió algo y ejecutamos el método echo que nos va a permitir obtener los campos de las búsquedas del usuario
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()


