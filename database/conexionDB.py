import mysql.connector

def db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password= "",
        database="cajero_automatico"
    )

    mycursor = mydb.cursor()

    return mydb, mycursor

def crearDatabase():
    mydb, mycursor = db()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS cajero_automatico")
    mycursor.execute("USE cajero_automatico")
    mycursor.execute("""CREATE TABLE IF NOT EXISTS cuentas_bancaria (
                        id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
                        numero_cuenta INT UNSIGNED NOT NULL,
                        clave INT UNSIGNED NOT NULL,
                        titular VARCHAR(50) NOT NULL,
                        saldo BIGINT UNSIGNED NOT NULL,
                        tipo_cuenta VARCHAR(50) NOT NULL,
                        create_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        update_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        PRIMARY KEY (id),
                        UNIQUE KEY numero_cuenta (numero_cuenta)
                    )""")
    
    mydb.commit()

    mycursor.close()


crearDatabase()
def verificar_conexion():
    try:
        # Establecer la conexión a la base de datos
        conexion = db()

        # Crear un cursor
        # Cursor es cuando hacemos el mysqli en php
        cursor = conexion.cursor()

        # Ejecutar una consulta SQL de prueba
        # el select 1 es una consulta de prueba a la base de datos
        cursor.execute('SELECT 1')

        # Recuperar los resultados
        resultados = cursor.fetchone()

        if resultados:
            print("La conexión a la base de datos se ha establecido correctamente.")
        else:
            print("La conexión a la base de datos no ha devuelto resultados.")

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)

# Verificar la conexión
# verificar_conexion()
# db()