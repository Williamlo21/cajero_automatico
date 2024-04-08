from controllers.tarjetaController import TarjetaController
from controllers.transaccionController import TransaccionController
from models.cuentaBancaria import CuentaBancaria
from controllers.cuentaBancariaController import CuentaBancariaController
class Retiro():
    @staticmethod
    def tipoDeRetiro():
        print("***********************************")
        print("...")
        print("Tipos de retiro. ")
        opciones = {
            "1" : "Retiro cuenta de ahorros.",
            "2" : "Retiro cuenta corriente.",
            "3" : "Retiro nequi.",
            "4" : "Retiro ahorro a la mano.",
            "5" : "Salir.",
        }
        
        for clave, valor in opciones.items():
            print(clave + ": " + valor)
        opcion = input("Digite el típo de retiro: ")
        Retiro().opcionRetiro(opcion)
        
    def opcionRetiro(self, opcion):
        opcion = int(opcion)
        if opcion == 1:
            confirmarTarjeta = TarjetaController.insertarTarjeta()
            tipoTarjeta = confirmarTarjeta[3]
            if tipoTarjeta == 'DEBITO':
                if confirmarTarjeta:
                    cuenta = CuentaBancaria.consultarCuenta(confirmarTarjeta)
                    tipoCuenta = cuenta[4]
                    if tipoCuenta == 'AHORRO':
                        seleccionarMonto = TransaccionController()
                        resultado = seleccionarMonto.seleccionaMonto(confirmarTarjeta)
                        if resultado:
                            opcion = resultado[0]
                            tarjeta = resultado[1]
                            transaccion = TransaccionController.opcionMonto(opcion, tarjeta)
                            if transaccion:
                                cuenta = transaccion[0]
                                monto = transaccion[1]
                                TransaccionController.imprimirRecibo(cuenta, monto)
                    else:
                        print("***********************************")
                        print("...")
                        print('En esta opcion solamente puede realizar retiros de cuentas de ahorro')
            else:
                print("***********************************")
                print("...")
                print("Su tarjeta es de Credito, para realizar avances seleccione la opción de realizar avances.")
        elif opcion == 2:
            confirmarTarjeta = TarjetaController.insertarTarjeta()
            tipoTarjeta = confirmarTarjeta[3]
            if tipoTarjeta == 'DEBITO':
                if confirmarTarjeta:
                    cuenta = CuentaBancaria.consultarCuenta(confirmarTarjeta)
                    tipoCuenta = cuenta[4]
                    if tipoCuenta == 'CORRIENTE':
                        seleccionarMonto = TransaccionController()
                        resultado = seleccionarMonto.seleccionaMonto(confirmarTarjeta)
                        if resultado:
                            opcion = resultado[0]
                            tarjeta = resultado[1]
                            transaccion = TransaccionController.opcionMonto(opcion, tarjeta)
                            if transaccion:
                                cuenta = transaccion[0]
                                monto = transaccion[1]
                                TransaccionController.imprimirRecibo(cuenta, monto)
                    else:
                        print("***********************************")
                        print("...")
                        print('En esta opcion solamente puede realizar retiros de cuentas de ahorro')
            else:
                print("***********************************")
                print("...")
                print("Su tarjeta es de Credito, para realizar avances seleccione la opción de realizar avances.")
        
        elif opcion == 3:
            print("***********************************")
            print("...")
            numero_cuenta = input("Digite su número de nequi: ")
            cuenta = CuentaBancariaController.consultarCuentaSinTarjeta(numero_cuenta)
            if cuenta:
                tipoCuenta = cuenta[4]
                if tipoCuenta == 'NEQUI':
                    codigo = TarjetaController.codigoMensaje()
                    if codigo:
                        opcion = TransaccionController.seleccionaMontoConCuenta()
                        if opcion:
                            monto = TransaccionController.opcionMontoConCuenta(opcion, numero_cuenta)
                            if monto:
                                retiro = CuentaBancariaController.realizarRetiroConCuenta(numero_cuenta, monto)
                                if retiro:
                                    TransaccionController.imprimirRecibo(cuenta, monto)
                else:
                    print("***********************************")
                    print("...")
                    print('En esta opcion solamente puede realizar retiros de Nequi')
            
        elif opcion == 4:
            print("***********************************")
            print("...")
            numero_cuenta = input("Digite su número de ahorro a la mano: ")
            cuenta = CuentaBancariaController.consultarCuentaSinTarjeta(numero_cuenta)
            if cuenta:
                tipoCuenta = cuenta[4]
                if tipoCuenta == 'A LA MANO':
                    codigo = TarjetaController.codigoMensaje()
                    if codigo:
                        opcion = TransaccionController.seleccionaMontoConCuenta()
                        if opcion:
                            monto = TransaccionController.opcionMontoConCuenta(opcion, numero_cuenta)
                            if monto:
                                retiro = CuentaBancariaController.realizarRetiroConCuenta(numero_cuenta, monto)
                                if retiro:
                                    TransaccionController.imprimirRecibo(cuenta, monto)
                else:
                    print("***********************************")
                    print("...")
                    print('En esta opcion solamente puede realizar retiros de Ahorro a la mano')
            
        elif opcion == 5:
            print("Gracias por visitarnos, ¡Vuelve pronto!")
        else:
            print("Por favor digite una opción valida")
            Retiro().tipoDeRetiro()


            
