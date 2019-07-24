'''
Vamos a comenzar a desarrollar una serie de codigos que nos sirvan para realizar peticiones a bases de datos mySQL, para comprobar la efectividad de estas medidas utilizando Python.
Desde la línea de comandos ejecutamos pip, instalar:
pip install mysql-connector

'''
import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="")

# a partir del objeto 'conexion1' que es de la clase 'MySQLConnection'
# llamamos al método 'cursor'

cursor1 = conexion1.cursor()

cursor1.execute("show databases")

for base in cursor1:
    print(base)
    
conexion1.close()

'''
Ahora proporcionamos otro codigo para poder realizar consultas a las bases de datos para obtener el nombre de las tablas que estan disponibles, y asi poder comenzar a realizar modificaciones sobre las mismas '''


print("Resultados de mysql.connector, referente a la consulta a las tablas disponibles en nuestras bases de datos:")

import mysql.connector

conexion2 = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='BHHA' )

cur = conexion2.cursor()

cur.execute( "Show Tables" )

for tabla in cur.fetchall() :
    print(tabla)
conexion2.close()

# Insertar filas en una tabla. Ahora implementaremos un programa que inserte un par de filas en la tabla 'BHAA_SPEAKERS'.

import mysql.connector

conexion3 = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='BHHA' )
cursor3 = conexion3.cursor()
sql = "INSERT INTO REGIONS(REGION_ID, REGION_NAME) VALUES (%s,%s)"
datos=("CONES", 8.0)
cursor3.execute(sql, datos)
datos=('TWITTERS', 4.0)
cursor3.execute(sql, datos)
datos=('SUB', 4.5)
cursor3.execute(sql, datos)
conexion3.commit()
conexion3.close()

# Eliminar una tabla. Ahora implementaremos un programa que  la tabla 'REGIONS de nuestra base de datos'.

# Insertar filas en una tabla. Ahora implementaremos un programa que inserte un par de filas en la tabla 'BHAA_SPEAKERS'.

import mysql.connector

conexion4 = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='BHHA' )
cursor4 = conexion3.cursor()
sql = "DROP TABLE REGIONS;"
cursor4.execute(sql)
conexion4.commit()
conexion4.close()

'''

Consulta contenido tablas

'''

import mysql.connector

conexion5 = mysql.connector.connect(host='localhost', user= 'root', passwd='', db='BHHA' )

cursor5=conexion5.cursor()
cursor5.execute("SELECT * FROM `hello_world`;")

for fila in cursor5.fetchall() :
    print(fila)
    
conexion5.close()

 '''
 Creamos una nueva tabla para comprobar de la efectividad de estas medidas y asi comprobar de la efectividad de las mismas.
 '''
import mysql.connector

conexion6 = mysql.connector.connect(host='localhost', user= 'root', passwd='', db='BHHA' )
cursor6 = conexion6.cursor()

conexion6.commit()
cursor6.execute("CREATE TABLE BHAA_PRUEBAS (id integer NOT NULL, password text, contact text, email text, friends text, time datetime DEFAULT '0000-00-00 00:00:00' NOT NULL, PRIMARY KEY (`id`));")
conexion6.close()

'''

Alterar la tabla generada

'''

import mysql.connector

conexion5 = mysql.connector.connect(host='localhost', user= 'root', passwd='', db='BHHA' )

cursor5=conexion5.cursor()
cursor5.execute("ALTER TABLE `BHAA_PRUEBAS` CHANGE `id` `id` INT(11) NOT NULL DEFAULT '250';")

for fila in cursor5:
    print(fila)
    
conexion5.close()

