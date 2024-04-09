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
    @staticmethod
    def registrarPagoServicio(cuenta, monto):
        conexion = Conexion()
        mycursor = conexion.mycursor
        cuentaOrigen = cuenta[0]
        saldo = monto
        dt = datetime.now()
        # ahora creamos la variable con la fecha de hoy
        fecha = dt.date()
        try:
            mycursor.execute("INSERT INTO transacciones (id, tipo_transaccion, cuenta_bancaria_origen_id, cuenta_bancaria_destino_id, saldo, descripcion, fecha) VALUES (null, 'PAGO', %s, null, %s, null, %s)", (cuentaOrigen, saldo, fecha))
            conexion.mydb.commit()
            return True
        except Exception as e:
            print("Error al registrar el pago:", e)
    @staticmethod
    def registrarAvance(cuenta, monto):
        conexion = Conexion()
        mycursor = conexion.mycursor
        cuentaOrigen = cuenta[0]
        saldo = monto
        dt = datetime.now()
        # ahora creamos la variable con la fecha de hoy
        fecha = dt.date()
        try:
            mycursor.execute("INSERT INTO transacciones (id, tipo_transaccion, cuenta_bancaria_origen_id, cuenta_bancaria_destino_id, saldo, descripcion, fecha) VALUES (null, 'AVANCE', %s, null, %s, null, %s)", (cuentaOrigen, saldo, fecha))
            conexion.mydb.commit()
            return True
        except Exception as e:
            print("Error al registrar el avance:", e)
    @staticmethod
    def registrarTransferencia(id_cuentaBancariaOrigen, id_cuentaBancariaDestino, saldo, descripcion):
        conexion = Conexion()
        mycursor = conexion.mycursor
        
        dt = datetime.now()
        # ahora creamos la variable con la fecha de hoy
        fecha = dt.date()
        try:
            mycursor.execute("INSERT INTO transacciones (id, tipo_transaccion, cuenta_bancaria_origen_id, cuenta_bancaria_destino_id, saldo, descripcion, fecha)\
                VALUES (null, 'TRANSFERENCIA', %s, %s, %s, %s, %s)", ( id_cuentaBancariaOrigen, id_cuentaBancariaDestino, saldo, descripcion, fecha,))
            conexion.mydb.commit()
            return True
        except Exception as e:
            print("Error al registrar el avance:", e)