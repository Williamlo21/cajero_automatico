from models.cuentaBancaria import CuentaBancaria

class CuentaBancariaController():
    
    @staticmethod
    def consultarCuentaSinTarjeta(numero_cuenta):
        cuenta = CuentaBancaria.consultarCuentaSinTarjeta(numero_cuenta)
        return cuenta
    @staticmethod
    def realizarRetiroConCuenta(numero_cuenta, monto):
        cuenta = CuentaBancaria.consultarCuentaSinTarjeta(numero_cuenta)
        retiro = CuentaBancaria.realizarRetiro(cuenta, monto)
        if retiro:
            return True