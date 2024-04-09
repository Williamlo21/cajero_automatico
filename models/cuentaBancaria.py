from database.conexionDB import Conexion
import decimal

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
        cuenta = tarjeta[2]
        conexion = Conexion()
        mycursor = conexion.mycursor
        mycursor.execute("SELECT * FROM cuenta_bancaria WHERE id = %s", (cuenta,))
        resultado = mycursor.fetchone()
        return resultado
    
    @staticmethod
    def realizarRetiro(cuenta, monto):
        idCuenta = cuenta[0]
        topeCuenta = cuenta[7]
        topeCuenta = decimal.Decimal(topeCuenta)
        tope = topeCuenta - monto
        montoCuenta = cuenta[3]
        montoDescontar = montoCuenta - monto
        conexion = Conexion()
        mycursor = conexion.mycursor
        try:    
            mycursor.execute("UPDATE cuenta_bancaria SET saldo = %s, tope = %s WHERE id = %s",(montoDescontar, tope, idCuenta,))
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
    @staticmethod
    def consultarCuentaSinTarjeta(numero_cuenta):
        conexion = Conexion()
        mycursor = conexion.mycursor
        mycursor.execute("SELECT * FROM cuenta_bancaria WHERE numero_cuenta = %s", (numero_cuenta,))
        resultado = mycursor.fetchone()
        return resultado
    @staticmethod
    def realizarTransferencia(id_cuentaBancariaOrigen, id_cuentaBancariaDestino, saldoCuentaDestino, topeCuentaOrigen, saldoCuentaOrigen):
        conexion = Conexion()
        mycursor = conexion.mycursor
        try:    
            # actualizar cuenta destino
            mycursor.execute("UPDATE cuenta_bancaria SET saldo = %s WHERE id = %s",(saldoCuentaDestino, id_cuentaBancariaDestino,))
            mycursor.execute("UPDATE cuenta_bancaria SET saldo = %s, tope = %s WHERE id = %s",(saldoCuentaOrigen, topeCuentaOrigen, id_cuentaBancariaOrigen,))
            conexion.mydb.commit()
            # actualizar cuenta origen
            
            return True
        except Exception as e:
            print("Error al realizar el retiro:", e)
# cuentaBancaria.store()