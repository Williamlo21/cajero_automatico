import mysql.connector

def db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password= "",
        database="cajero_automatico"
    )

def verificar_conexion():
    try:
        # Establecer la conexión a la base de datos
        conexion = db()

        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar una consulta SQL de prueba
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
verificar_conexion()