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
    @staticmethod
    def consultarCuentaConTarjeta(tarjeta):
        cuenta = CuentaBancaria.consultarCuenta(tarjeta)
        if cuenta:
            return cuenta
    @staticmethod
    def realizarTransferencia(id_cuentaBancariaOrigen, id_cuentaBancariaDestino, saldoCuentaDestino, saldoCuentaOrigen,topeCuentaOrigen):
        
        transferencia = CuentaBancaria.realizarTransferencia(id_cuentaBancariaOrigen, id_cuentaBancariaDestino, saldoCuentaDestino, topeCuentaOrigen, saldoCuentaOrigen)
        if transferencia:
            return True
    
    @staticmethod
    def consultarCuentaConNumero(numeroCuenta):
        cuentaBancariaDestino = CuentaBancaria.consultarCuentaUser(numeroCuenta)
        if cuentaBancariaDestino:
            return cuentaBancariaDestino
    @staticmethod
    def realizarRetiro(cuenta, factura):
        pago = CuentaBancaria.realizarRetiro(cuenta, factura)
        if pago:
            return True
    @staticmethod
    def consultarSaldo(cuenta):
        saldo = CuentaBancaria.consultarSaldo(cuenta)
        if saldo:
            return saldo