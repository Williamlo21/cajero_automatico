from models.servicios import Servicio
from controllers.tarjetaController import TarjetaController
from controllers.cuentaBancariaController import CuentaBancariaController
from controllers.transaccionController import TransaccionController
class ServicioController():
    @staticmethod
    def obtenerReferencia():

        print("Escanee el codigo de barras o ingrese la referencia de pago.")
        while True:
            referencia = input("referencia: ")
            if referencia:
                return referencia
            else:
                print("Por favor ingrese una referencia valida.")
            
    
    @staticmethod
    def comenzarPago():
        print("*******************")
        print("*Pago de servicios*")
        print("*******************")
        referencia = ServicioController.obtenerReferencia()
        if referencia:
            servicio = Servicio.consultarServicio(referencia)
            confirmar = ServicioController.mostrarServicio(servicio)
            if confirmar:
                metodo = ServicioController.metodoDePago()
                if metodo:
                    ServicioController.validarMetodoPago(metodo, servicio)
    @staticmethod
    def mostrarServicio(servicio):
        print("***********************************")
        print("...")
        referencia = servicio[1]
        reciboPago = servicio[2]
        factura = servicio[3]
        print("Referencia: ", referencia)
        print("Factura: ", factura)
        print("Valor factura: ", reciboPago)
        print("***********************************")
        print("...")
        respuesta = input("Desea continuar? ")
        respuesta = int(respuesta)
        if respuesta == 1:
            return True
        else:
            print("Gracias por visitarnos, ¡Vuelve pronto!")
    @staticmethod
    def metodoDePago():
        print("***********************************")
        print("...")
        print("Metodo de pago ")
        opciones = {
            "1" : "Tarjeta debito",
            "2" : "Tarjeta credito",
            "3" : "Nequi",
            "4" : "Ahorro a la mano.",
            "5" : "Salir.",
        }
        
        opcion_valida = False
        while not opcion_valida:
            for clave, valor in opciones.items():
                print(clave + ": " + valor)
            opcion = input("Digite el monto a retirar: ")
            if opcion in opciones.keys():
                opcion_valida = True
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

        return opcion
    @staticmethod
    def validarMetodoPago(metodo, servicio):
        metodo = int(metodo)
        if metodo == 1:
            tarjeta = TarjetaController.insertarTarjeta()
            if tarjeta:
                tipoTarjeta = tarjeta[3]
                if tipoTarjeta == 'DEBITO':
                    cuenta = CuentaBancariaController.consultarCuentaConTarjeta(tarjeta)
                    if cuenta:
                        saldoCuenta = cuenta[3]
                        saldoCuenta = float(saldoCuenta)
                        topeCuenta = cuenta[7]
                        topeCuenta = float(topeCuenta)
                        factura = servicio[3]
                        factura = float(factura)
                        if saldoCuenta >= factura:
                            if topeCuenta >= factura:
                                pago = CuentaBancariaController.realizarRetiro(cuenta, factura)
                                if pago:
                                    transaccion = TransaccionController.registrarPagoServicio
                                    if transaccion:
                                        TransaccionController.imprimirReciboPago(cuenta, factura)
                            else:
                                print("***********************************")
                                print("...")
                                print("Tope diario superado.")
                        else:
                            print("***********************************")
                            print("...")
                            print("Saldo insuficiente.")
                else:
                    print("***********************************")
                    print("...")
                    print("Su tarjeta es de Credito, para hacer pagos con tarjeta de credito seleccione la opción.")
        elif metodo == 2:
            tarjeta = TarjetaController.insertarTarjeta()
            if tarjeta:
                tipoTarjeta = tarjeta[3]
                if tipoTarjeta == 'CREDITO':
                    cuenta = CuentaBancariaController.consultarCuentaConTarjeta(tarjeta)
                    if cuenta:
                        saldoCuenta = cuenta[3]
                        saldoCuenta = float(saldoCuenta)
                        topeCuenta = cuenta[7]
                        topeCuenta = float(topeCuenta)
                        factura = servicio[3]
                        factura = float(factura)
                        if saldoCuenta >= factura:
                            if topeCuenta >= factura:
                                pago = CuentaBancariaController.realizarRetiro(cuenta, factura)
                                if pago:
                                    transaccion = TransaccionController.registrarPagoServicio
                                    if transaccion:
                                        TransaccionController.imprimirReciboPago(cuenta, factura)
                            else:
                                print("***********************************")
                                print("...")
                                print("Tope diario superado.")
                        else:
                            print("***********************************")
                            print("...")
                            print("Saldo insuficiente.")
                else:
                    print("***********************************")
                    print("...")
                    print("Su tarjeta es debito, para hacer pagos con tarjeta debito seleccione la opción.")
        elif metodo == 3:
            print("***********************************")
            print("...")
            numero_cuenta = input("Digite su número de nequi: ")
            cuenta = CuentaBancariaController.consultarCuentaSinTarjeta(numero_cuenta)
            if cuenta:
                tipoCuenta = cuenta[4]
                if tipoCuenta == 'NEQUI':
                    saldoCuenta = cuenta[3]
                    saldoCuenta = float(saldoCuenta)
                    topeCuenta = cuenta[7]
                    topeCuenta = float(topeCuenta)
                    factura = servicio[3]
                    factura = float(factura)
                    if saldoCuenta >= factura:
                        if topeCuenta >= factura:
                            pago = CuentaBancariaController.realizarRetiro(cuenta, factura)
                            if pago:
                                transaccion = TransaccionController.registrarPagoServicio
                                if transaccion:
                                    TransaccionController.imprimirReciboPago(cuenta, factura)
                        else:
                            print("***********************************")
                            print("...")
                            print("Tope diario superado.")
                    else:
                        print("***********************************")
                        print("...")
                        print("Saldo insuficiente.")
                else:
                    print("***********************************")
                    print("...")
                    print("Esta opción es solo para pagos de servicios con nequi.")
        elif metodo == 4:
            print("***********************************")
            print("...")
            numero_cuenta = input("Digite su número de nequi: ")
            cuenta = CuentaBancariaController.consultarCuentaSinTarjeta(numero_cuenta)
            if cuenta:
                tipoCuenta = cuenta[4]
                if tipoCuenta == 'A LA MANO':
                    saldoCuenta = cuenta[3]
                    saldoCuenta = float(saldoCuenta)
                    topeCuenta = cuenta[7]
                    topeCuenta = float(topeCuenta)
                    factura = servicio[3]
                    factura = float(factura)
                    if saldoCuenta >= factura:
                        if topeCuenta >= factura:
                            pago = CuentaBancariaController.realizarRetiro(cuenta, factura)
                            if pago:
                                transaccion = TransaccionController.registrarPagoServicio(cuenta, factura)
                                if transaccion:
                                    TransaccionController.imprimirReciboPago(cuenta, factura)
                        else:
                            print("***********************************")
                            print("...")
                            print("Tope diario superado.")
                    else:
                        print("***********************************")
                        print("...")
                        print("Saldo insuficiente.")
                else:
                    print("***********************************")
                    print("...")
                    print("Esta opción es solo para pagos de servicios con bancolombia a la mano.")
        elif metodo == 5:
            print("Gracias por visitarnos, ¡Vuelve pronto!")
        else:
            print("Opción invalida.")