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
    def realizarTransferencia(cuentaBancariaOrigen, cuentaBancariaDestino,saldoCuentaOrigen,topeCuentaOrigen, monto):
        id_cuentaBancariaOrigen = cuentaBancariaOrigen[0]
        llaveCuentaDestino = cuentaBancariaDestino.split(" - ")
        id_cuentaBancariaDestino = llaveCuentaDestino[0]
        numeroCuentaDestino = llaveCuentaDestino[1]
        saldoCuentaDestino = llaveCuentaDestino[5]
        saldoCuentaDestino = float(saldoCuentaDestino)
        saldoCuentaDestino = saldoCuentaDestino + monto
        transferencia = CuentaBancaria.realizarTransferencia(id_cuentaBancariaOrigen, id_cuentaBancariaDestino, saldoCuentaDestino, topeCuentaOrigen, saldoCuentaOrigen)
        if transferencia:
            return id_cuentaBancariaDestino, id_cuentaBancariaOrigen, numeroCuentaDestino
    @staticmethod
    def consultarCuentaConNumero(numeroCuenta):
        cuentaBancariaDestino = CuentaBancaria.consultarCuentaSinTarjeta(numeroCuenta)
        if cuentaBancariaDestino:
            return cuentaBancariaDestino