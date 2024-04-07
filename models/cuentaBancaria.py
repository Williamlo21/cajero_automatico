from database.conexionDB import Conexion

class CuentaBancaria():

    def __init__(self, id, numero_cuenta, clave, titular, saldo, tipo_cuenta ):
        self.__Conexion = Conexion()
        self.id = id
        self.numero_cuenta = numero_cuenta
        self.clave = clave
        self.titular = titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta
    @staticmethod
    def consultarCuenta(tarjeta):
        cuenta = tarjeta[0]
        conexion = Conexion()
        mycursor = conexion.mycursor
        mycursor.execute("SELECT * FROM cuenta_bancaria WHERE id = %s", (cuenta,))
        resultado = mycursor.fetchone()
        return resultado
    @staticmethod
    def realizarRetiro(cuenta, monto):
        idCuenta = cuenta[0]
        topeCuenta = cuenta[7]
        tope = topeCuenta - monto
        conexion = Conexion()
        mycursor = conexion.mycursor
        try:    
            mycursor.execute("UPDATE cuenta_bancaria SET saldo = %s, tope = %s WHERE id = %s",(monto, tope, idCuenta,))
            conexion.mydb.commit()
            return True
        except Exception as e:
            print("Error al realizar el retiro:", e)
    @staticmethod
    def consultarSaldo(cuenta):
        idCuenta = cuenta[1]
        conexion = Conexion()
        mycursor = conexion.mycursor
        mycursor.execute("SELECT * FROM cuenta_bancaria WHERE id = %s", (idCuenta,))
        resultado = mycursor.fetchone()
        return resultado
# cuentaBancaria.store()