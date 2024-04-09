from controllers.tarjetaController import TarjetaController
from controllers.cuentaBancariaController import CuentaBancariaController
from controllers.cuentainscritaController import CuentaInscritaController
from controllers.transaccionController import TransaccionController
class TransferenciaController():
    
    @staticmethod
    def principal():
        print("***********************************")
        print("...")
        menuCuenta = TransferenciaController.menuCuentas()
        if menuCuenta:
            TransferenciaController.opcionCuentas(menuCuenta)
        
        
    @staticmethod
    def menuTransferencias():
        opciones = {
            "1" : "Cuenta inscrita.",
            "2" : "Cuenta no inscrita.",
        }
        
        opcion_valida = False
        while not opcion_valida:
            for clave, valor in opciones.items():
                print(clave + ": " + valor)
            opcion = input("Digite la opción: ")
            if opcion in opciones.keys():
                opcion_valida = True
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        return opcion
    
    @staticmethod
    def opcionMenu(opcion, cuentaOrigen):
        opcion = int(opcion)
        if opcion == 1:

            cuentasInscritas = CuentaInscritaController.consultarCuentasInscritas(cuentaOrigen)
            if cuentasInscritas:
                # TransferenciaController.mostrarCuentasinscritas(cuentasInscritas)
                opciones = CuentaInscritaController.mostrarCuentasInscritas(cuentasInscritas)
                if opciones:
                    cuentaBancariaDestino = CuentaInscritaController.escogerCuentaInscrita(opciones)
                    if cuentaBancariaDestino:
                        cuentaBancariaDestino = str(cuentaBancariaDestino)
                        cuentaBancariaDestino = opciones[cuentaBancariaDestino]
                        monto = TransferenciaController.solicitarMonto()
                        if monto:
                            saldoCuentaOrigen = cuentaOrigen[3]
                            topeCuentaOrigen = cuentaOrigen[7]
                            if saldoCuentaOrigen >= monto:
                                if topeCuentaOrigen >= monto:
                                    saldoCuentaOrigen = float(saldoCuentaOrigen)
                                    saldoCuentaOrigen = saldoCuentaOrigen - monto
                                    topeCuentaOrigen = float(topeCuentaOrigen)
                                    topeCuentaOrigen = topeCuentaOrigen - monto
                                    descripcion = TransferenciaController.obtenerDescripcion()
                                    transferencia = CuentaBancariaController.realizarTransferencia(cuentaOrigen, cuentaBancariaDestino,saldoCuentaOrigen, topeCuentaOrigen, monto)
                                    if transferencia:
                                        id_cuentaBancariaDestino = transferencia[0]
                                        id_cuentaBancariaOrigen = transferencia[1]
                                        numeroCuentaDestino = transferencia[2]
                                        transaccion = TransaccionController.registrarTransferencia(id_cuentaBancariaOrigen, id_cuentaBancariaDestino, monto, descripcion)
                                        if transaccion:
                                            numeroCuentaOrigen = cuentaOrigen[1]
                                            TransaccionController.imprimirReciboTransferencia(numeroCuentaOrigen,numeroCuentaDestino,monto, descripcion)
                                else:
                                    print("Tope diario superado.")
                            else:
                                print("Saldo insuficiente.")
        elif opcion == 2:
            print("Cuentas no inscritas")
    @staticmethod
    def obtenerDescripcion():
        print("***********************************")
        print("...")
        while True:
            descripcion = input("Descripción: ")
            if descripcion:
                return descripcion
            else:
                print("Por favor ingrese una descripción.")
    @staticmethod
    def solicitarMonto():
        print("***********************************")
        print("...")
        while True:
            monto = input("Digite el valor a transferir: ")
            try:
                monto = float(monto)
                if monto > 0:
                    return monto
                else:
                    print("Ingrese un valor positivo.")
            except ValueError:
                print("Ingrese un número entero positivo.")
        
    def menuCuentas():
        opciones = {
            "1" : "Cuenta de ahorros",
            "2" : "Cuenta Corriente",
            "3" : "Nequi",
            "4" : "Ahorro a la mano",
        }
        
        opcion_valida = False
        while not opcion_valida:
            for clave, valor in opciones.items():
                print(clave + ": " + valor)
            opcion = input("Digite su cuenta: ")
            if opcion in opciones.keys():
                opcion_valida = True
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        return opcion
    @staticmethod
    def opcionCuentas(opcion):
        opcion = int(opcion)
        if opcion == 1:
            tarjeta = TarjetaController.insertarTarjeta()
            if tarjeta:
                tipoTarjeta = tarjeta[3]
                if tipoTarjeta == 'DEBITO':
                    cuenta = CuentaBancariaController.consultarCuentaConTarjeta(tarjeta)
                    tipoCuenta = cuenta[4]
                    if tipoCuenta == 'AHORRO':
                        opcion = TransferenciaController.menuTransferencias()
                        TransferenciaController.opcionMenu(opcion, cuenta)
                    else:
                        print("***********************************")
                        print("...")
                        print('En esta opcion solamente puede realizar transferencias desde cuentas de ahorro')
                else:
                    print("***********************************")
                    print("...")
                    print("Su tarjeta es de Credito, para realizar avances seleccione la opción de realizar avances.")
        elif opcion == 2:
            tarjeta = TarjetaController.insertarTarjeta()
            tipoTarjeta = tarjeta[3]
            if tipoTarjeta == 'DEBITO':
                if tarjeta:
                    cuenta = CuentaBancariaController.consultarCuentaConTarjeta(tarjeta)
                    tipoCuenta = cuenta[4]
                    if tipoCuenta == 'CORRIENTE':
                        opcion = TransferenciaController.menuTransferencias()
                        TransferenciaController.opcionMenu(opcion)
                    else:
                        print("***********************************")
                        print("...")
                        print('En esta opcion solamente puede realizar transferencias desde cuentas corriente')
            else:
                print("***********************************")
                print("...")
                print("Su tarjeta es de Credito, para realizar avances seleccione la opción de realizar avances.")
        # elif opcion == 3:
        #     print("***********************************")
        #     print("...")
        #     numero_cuenta = input("Digite su número de nequi: ")
        #     cuenta = CuentaBancariaController.consultarCuentaSinTarjeta(numero_cuenta)
        #     if cuenta:
        #         tipoCuenta = cuenta[4]
        #         if tipoCuenta == 'NEQUI':
        #             codigo = TarjetaController.codigoMensaje()
        #             if codigo:
        #                 opcion = TransaccionController.seleccionaMontoConCuenta()
        #                 if opcion:
        #                     monto = TransaccionController.opcionMontoConCuenta(opcion, numero_cuenta)
        #                     if monto:
        #                         retiro = CuentaBancariaController.realizarRetiroConCuenta(numero_cuenta, monto)
        #                         if retiro:
        #                             TransaccionController.imprimirRecibo(cuenta, monto)
        #         else:
        #             print("***********************************")
        #             print("...")
        #             print('En esta opcion solamente puede realizar retiros de Nequi')
            
        # elif opcion == 4:
        #     print("***********************************")
        #     print("...")
        #     numero_cuenta = input("Digite su número de ahorro a la mano: ")
        #     cuenta = CuentaBancariaController.consultarCuentaSinTarjeta(numero_cuenta)
        #     if cuenta:
        #         tipoCuenta = cuenta[4]
        #         if tipoCuenta == 'A LA MANO':
        #             codigo = TarjetaController.codigoMensaje()
        #             if codigo:
        #                 opcion = TransaccionController.seleccionaMontoConCuenta()
        #                 if opcion:
        #                     monto = TransaccionController.opcionMontoConCuenta(opcion, numero_cuenta)
        #                     if monto:
        #                         retiro = CuentaBancariaController.realizarRetiroConCuenta(numero_cuenta, monto)
        #                         if retiro:
        #                             TransaccionController.imprimirRecibo(cuenta, monto)
        #         else:
        #             print("***********************************")
        #             print("...")
        #             print('En esta opcion solamente puede realizar retiros de Ahorro a la mano')