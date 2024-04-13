import mysql.connector

# conexion
class Conexion():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cajero_automatico"
        )

        self.mycursor = self.mydb.cursor()
        # funcion para crear la base de datos
        # self.mycursor = self.crearDatabase()
        

    def crearDatabase(self):

        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS cajero_automatico")
        self.mycursor.execute("USE cajero_automatico")
        self.mycursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            nombres VARCHAR(50) NOT NULL,
            apellidos VARCHAR(50) NOT NULL,
            numero_documento VARCHAR(50) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY usuario_unico (nombres, apellidos, numero_documento))""")
        self.mycursor.execute("""
            CREATE TABLE IF NOT EXISTS cuenta_bancaria (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            numero_cuenta INT UNSIGNED NOT NULL,
            user_titular_id VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
            saldo DECIMAL(20, 2) UNSIGNED NOT NULL,
            tipo_cuenta ENUM('AHORRO', 'NEQUI', 'A LA MANO', 'CREDITO') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
            create_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            update_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            tope DECIMAL(20, 2) NOT NULL DEFAULT '2000000.00',
            PRIMARY KEY (id),
            UNIQUE KEY cuenta_unica (numero_cuenta) USING BTREE)""")
        
        self.mycursor.execute("""CREATE TABLE IF NOT EXISTS cuentas_inscritas (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            cuenta_bancaria_id BIGINT UNSIGNED NOT NULL,
            cuenta_bancaria_inscrita_id BIGINT UNSIGNED NOT NULL,
            create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            update_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            UNIQUE KEY cuenta_inscrita_unica (cuenta_bancaria_id, cuenta_bancaria_inscrita_id),
            KEY FK_cuentas_inscritas_cuenta_bancaria_2 (cuenta_bancaria_inscrita_id),
            CONSTRAINT FK_cuentas_inscritas_cuenta_bancaria FOREIGN KEY (cuenta_bancaria_id) REFERENCES cuenta_bancaria (id) ON DELETE CASCADE ON UPDATE CASCADE,
            CONSTRAINT FK_cuentas_inscritas_cuenta_bancaria_2 FOREIGN KEY (cuenta_bancaria_inscrita_id) REFERENCES cuenta_bancaria (id) ON DELETE CASCADE ON UPDATE CASCADE)""")
        self.mycursor.execute("""CREATE TABLE IF NOT EXISTS tarjetas (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            numero_tarjeta INT UNSIGNED NOT NULL,
            cuenta_bancaria_id BIGINT UNSIGNED NOT NULL,
            tipo_tarjeta ENUM('CREDITO', 'DEBITO') NOT NULL,
            fecha_vencimiento DATE DEFAULT NULL,
            codigo_cvc INT NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY tarjeta_unica (numero_tarjeta),
            KEY FK_tarjetas_cuenta_bancaria (cuenta_bancaria_id),
            CONSTRAINT FK_tarjetas_cuenta_bancaria FOREIGN KEY (cuenta_bancaria_id) REFERENCES cuenta_bancaria (id) ON DELETE CASCADE ON UPDATE CASCADE)""")
        self.mycursor.execute("""CREATE TABLE IF NOT EXISTS transacciones (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            tipo_transaccion ENUM('TRANSFERENCIA', 'RETIRO', 'AVANCE', 'PAGO') NOT NULL,
            cuenta_bancaria_origen_id BIGINT UNSIGNED NOT NULL,
            cuenta_bancaria_destino_id BIGINT UNSIGNED DEFAULT NULL,
            saldo DECIMAL(20, 2) UNSIGNED NOT NULL,
            descripcion VARCHAR(50) NOT NULL,
            fecha DATE NOT NULL ,
            create_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            update_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            KEY FK_transacciones_cuenta_bancaria (cuenta_bancaria_origen_id),
            KEY FK_transacciones_cuenta_bancaria_2 (cuenta_bancaria_destino_id),
            CONSTRAINT FK_transacciones_cuenta_bancaria FOREIGN KEY (cuenta_bancaria_origen_id) REFERENCES cuenta_bancaria (id) ON DELETE CASCADE ON UPDATE CASCADE,
            CONSTRAINT FK_transacciones_cuenta_bancaria_2 FOREIGN KEY (cuenta_bancaria_destino_id) REFERENCES cuenta_bancaria (id) ON DELETE CASCADE ON UPDATE CASCADE)""")
        self.mydb.commit()
        self.mycursor.close()

    def verificar_conexion():
        try:
            # Establecer la conexión a la base de datos
            conexion = Conexion.db()

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
    # verificar_conexion()


conexion = Conexion()
# conexion.crearDatabase()