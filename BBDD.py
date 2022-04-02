"""
-Clase: BBDD.py
-Descripción: Clase en la cual se conecta con la base de datos y se establecen todas
    las funciones que realizan consultas tanto con la tabla BBDD la cual guarda información
    sobre todas las playas de España y la tabla suscrito la cual guarda información sobre
    las playas a las que esta suscrito cada usuario
"""

#Libreria para el acceso a la base de datos
import pymysql

#Base de datos de playas
database_host = 'bnhukxmv5yeixvtezd51-mysql.services.clever-cloud.com' 
username = 'uhvo87uj6up0zzym' 
password = 'Qlh2E0viyQFPSEdQ6PHc' 
database_name = 'bnhukxmv5yeixvtezd51' 


#Conexion con la base de datos usando los datos previos
db = pymysql.connect(host= database_host,
                            user=username,
                            password=password,
                            database=database_name,
                            charset='utf8mb4')



#Insercción de datos nuevos en la tabla de suscripcion
def insertar(chat_id, user_first_name ,nombre, provincia, municipio, x,y):
    db.ping(reconnect = True)
    cursor = db.cursor()

    cursor.execute("INSERT INTO suscrito (ID,Usuario,Nombre,Provincia,Municipio,CX,CY) VALUES (%s,%s,%s,%s,%s,%s,%s)", (chat_id, user_first_name ,nombre, provincia, municipio, x,y) )
    cursor.fetchall()    

    db.commit()

    


#Busqueda en la base de datos playas que contengan la palabra de la playa indicada
def buscar(playa):
    db.ping(reconnect = True)
    cursor = db.cursor()
   
    cursor.execute("SET @playa = (%s)",playa)
    count = cursor.execute("SELECT Coordenada_X,Coordenada_Y,Zona_Surf,Provincia,Termino_Municipal,Nombre FROM BBDD WHERE Nombre LIKE CONCAT('%' , @playa , '%') ")
    result=cursor.fetchall()
  
    return result,count


#Busqueda de playas suscritas para un usuario en un chat
def buscarNomMun(chat_id, user_first_name):
    db.ping(reconnect = True)
    cursor = db.cursor()

    count = cursor.execute("SELECT Nombre,Municipio,Provincia,CX,CY FROM suscrito WHERE ID = (%s) AND Usuario = (%s) ", (chat_id, user_first_name))
    result=cursor.fetchall()

    return count,result


#Busqueda de todos los usuarios que estan suscritos a alguna playa
def subs_auto():
    db.ping(reconnect = True)
    cursor = db.cursor()

    count = cursor.execute("SELECT DISTINCT ID,Usuario FROM suscrito ")
    result=cursor.fetchall()

    return count,result


#Selección de una playa en función de las coordenadas introducidas
def buscarCoo(x,y):
    db.ping(reconnect = True)
    cursor = db.cursor()

    count = cursor.execute("SELECT Nombre,Provincia,Termino_Municipal FROM BBDD WHERE Coordenada_Y = (%s) and Coordenada_X = (%s)" , (str(x) , str(y) ))
    result=cursor.fetchall()

    return count,result


#Usuario elimina la playa que determine de sus playas suscritas
def eliminar(chat_id, user_first_name, n, m, p, cx, cy):
    db.ping(reconnect = True)
    cursor = db.cursor()
    
    cursor.execute("DELETE FROM suscrito WHERE ID = (%s) AND Usuario = (%s) AND Nombre = (%s) AND Municipio = (%s) AND Provincia = (%s) AND CX = (%s) AND CY = (%s)" , (chat_id, user_first_name, n, m, p, cx, cy  ))
    cursor.fetchall()

    db.commit()



#Busqueda de las playas a las que estan suscritas todos los usuarios
def playas_subs():
    db.ping(reconnect = True)
    cursor=db.cursor()
    
    count = cursor.execute("SELECT DISTINCT Nombre,Provincia,CX,CY FROM suscrito")
    result = cursor.fetchall()

    return count,result



#Busqueda de la infromación de la playa en funcion de sus coordenadas
def info_playa(x,y):
    db.ping(reconnect = True)
    cursor=db.cursor()
    
    count = cursor.execute("SELECT * FROM BBDD WHERE Coordenada_Y = (%s) and Coordenada_X = (%s)" , (str(x),str(y)) )
    result = cursor.fetchall()

    return result
