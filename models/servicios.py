from database.conexionDB import Conexion
class Servicio():
    @staticmethod
    def consultarServicio(referencia):
        conexion = Conexion()
        mycursor = conexion.mycursor

        mycursor.execute("SELECT * FROM servicios WHERE referencia = %s", (referencia,))
        servicio = mycursor.fetchone()
        if servicio:
            return servicio
        else:
            print("***********************************")
            print("...")
            print("La referencia de pago del servicio no existe.")
    