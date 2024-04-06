from database.conexionDB import Conexion

class cuentaBancaria():

    def __init__(self, id, numero_cuenta, clave, titular, saldo, tipo_cuenta ):
        self.__Conexion = Conexion()
        self.id = id
        self.numero_cuenta = numero_cuenta
        self.clave = clave
        self.titular = titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta

    def store():
        print("hola mundo")


cuentaBancaria.store()