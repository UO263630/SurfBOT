
#Libreria para el acceso a la base de datos
import pymysql

#Base de datos de playas
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

def insertar(chat_id, user_first_name ,nombre, provincia, municipio, x,y):
    cursor = db.cursor()

    count = cursor.execute("INSERT INTO suscrito (ID,Usuario,Nombre,Provincia,Municipio,CX,CY) VALUES (%s,%s,%s,%s,%s,%s,%s)", (chat_id, user_first_name ,nombre, provincia, municipio, x,y) )
    result=cursor.fetchall()

    db.commit()



def buscar(playa):
    cursor = db.cursor()

    count = cursor.execute("SELECT Coordenada_X,Coordenada_Y,Zona_Surf,Provincia,Termino_Municipal FROM BBDD WHERE Nombre = (%s) " ,playa )
    result=cursor.fetchall()
    #print(result)

    return result,count



def buscarNomMun(chat_id, user_first_name):
    cursor = db.cursor()

    count = cursor.execute("SELECT Nombre,Municipio,Provincia,CX,CY FROM suscrito WHERE ID = (%s) AND Usuario = (%s) ", (chat_id, user_first_name))
    result=cursor.fetchall()

    return count,result

def subs_auto():
    cursor = db.cursor()

    count = cursor.execute("SELECT ID,Usuario FROM suscrito ")
    result=cursor.fetchall()

    return count,result




def buscarCoo(x,y):
    cursor = db.cursor()

    count = cursor.execute("SELECT Nombre,Provincia,Termino_Municipal FROM BBDD WHERE Coordenada_Y = (%s) and Coordenada_X = (%s)" , (str(x) , str(y) ))
    result=cursor.fetchall()

    return count,result


def eliminar(chat_id, user_first_name, n, m, p, cx, cy):
    cursor = db.cursor()
    
    cursor.execute("DELETE FROM suscrito WHERE ID = (%s) AND Usuario = (%s) AND Nombre = (%s) AND Municipio = (%s) AND Provincia = (%s) AND CX = (%s) AND CY = (%s)" , (chat_id, user_first_name, n, m, p, cx, cy  ))
    cursor.fetchall()

    db.commit()

def buscarS(chat_id, user_first_name):
    cursor = db.cursor()

    count = cursor.execute("SELECT * FROM suscrito WHERE ID = (%s) AND Usuario = (%s) ", (chat_id, user_first_name))
    result=cursor.fetchall()

    return count,result


#db.close()


