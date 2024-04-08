from database.conexionDB import Conexion
from datetime import datetime
class Transaccion:
    
    @staticmethod
    def registrarRetiro(cuenta, monto):
        conexion = Conexion()
        mycursor = conexion.mycursor
        cuentaOrigen = cuenta[0]
        saldo = monto
        dt = datetime.now()
        # ahora creamos la variable con la fecha de hoy
        fecha = dt.date()
        try:
            mycursor.execute("INSERT INTO transacciones (id, tipo_transaccion, cuenta_bancaria_origen_id, cuenta_bancaria_destino_id, saldo, descripcion, fecha) VALUES (null, 'RETIRO', %s, null, %s, null, %s)", (cuentaOrigen, saldo, fecha))
            conexion.mydb.commit()
            return True
        except Exception as e:
            print("Error al registrar el retiro:", e)