from database.conexionDB import Conexion
from datetime import datetime

class Tarjeta():
    def __init__(self):
        # Crear una instancia de la clase Conexion para establecer la conexión
        self.conexion = Conexion()
    
    def existeTarjeta(self, tarjeta):
        mycursor = self.conexion.mycursor
        mycursor.execute("SELECT * FROM tarjetas WHERE numero_tarjeta = %s", (tarjeta,))
        resultado = mycursor.fetchone()

        if resultado:
            # fecha de vencimiento es el item 4
            fecha_vencimiento = resultado[4]
            # instanciamos el objeto datetime.now
            dt = datetime.now()
            # ahora creamos la variable con la fecha de hoy
            now = dt.date()
            print("Tarjeta leida con exíto.")
            print("Validando la tarjeta, por favor espere.")
            print("...")
            if fecha_vencimiento > now:
                print("Tarjeta activa.")
                return resultado
            else:
                print("Tarjeta vencida, por favor comuniquese con su banco.")
                print("Gracias por preferirnos.")
    
        else:
            print("Tarjeta invalida.")
    @staticmethod
    def cambiarClaveTarjeta(nuevaClave, numero_tarjeta):
        conexion = Conexion()
        mycursor = conexion.mycursor
        try:    
            # actualizar clave
            mycursor.execute("UPDATE tarjetas SET clave = %s WHERE numero_tarjeta = %s",(nuevaClave, numero_tarjeta,))
            conexion.mydb.commit()
            
            return True
        except Exception as e:
            print("Error al cambiar la clave:", e)
    