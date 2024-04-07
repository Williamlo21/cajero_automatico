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
        # fecha de vencimiento es el item 4
        fecha_vencimiento = resultado[4]
        tipo_tarjeta = resultado[3]
        # instanciamos el objeto datetime.now
        dt = datetime.now()
        # ahora creamos la variable con la fecha de hoy
        now = dt.date()

        if resultado:
            print("Tarjeta leida con exíto.")
            print("Validando la tarjeta, por favor espere.")
            print("...")
            if tipo_tarjeta == 'DEBITO':
                if fecha_vencimiento > now:
                    print("Tarjeta activa.")
                    return resultado
                else:
                    print("Tarjeta vencida, por favor comuniquese con su banco.")
                    print("Gracias por preferirnos.")
            else:
                print("Su tarjeta es de credito.")
                print("Para realizar avances, seleccione la opción de realizar avance en el menú principal.")
        else:
            print("Tarjeta invalida.")