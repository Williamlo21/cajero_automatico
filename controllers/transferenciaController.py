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
                                    id_cuentaBancariaOrigen = cuentaOrigen[0]
                                    llaveCuentaDestino = cuentaBancariaDestino.split(" - ")
                                    id_cuentaBancariaDestino = llaveCuentaDestino[0]
                                    numeroCuentaDestino = llaveCuentaDestino[1]
                                    saldoCuentaDestino = llaveCuentaDestino[5]
                                    saldoCuentaDestino = float(saldoCuentaDestino)
                                    saldoCuentaDestino = saldoCuentaDestino + monto
                                    transferencia = CuentaBancariaController.realizarTransferencia(id_cuentaBancariaOrigen, id_cuentaBancariaDestino, saldoCuentaDestino, saldoCuentaOrigen, topeCuentaOrigen)
                                    if transferencia:
                                        transaccion = TransaccionController.registrarTransferencia(id_cuentaBancariaOrigen, id_cuentaBancariaDestino, monto, descripcion)
                                        if transaccion:
                                            numeroCuentaOrigen = cuentaOrigen[1]
                                            TransaccionController.imprimirReciboTransferencia(numeroCuentaOrigen,numeroCuentaDestino,monto, descripcion)
                                else:
                                    print("Tope diario superado.")
                            else:
                                print("Saldo insuficiente.")
        elif opcion == 2:
            numeroCuenta = TransferenciaController.obtenerNumeroCuenta()
            cuentaBancariaDestino = CuentaBancariaController.consultarCuentaConNumero(numeroCuenta)
            if cuentaBancariaDestino:
                confirmar = TransferenciaController.mostrarCuenta(cuentaBancariaDestino)
                if confirmar:
                    monto = TransferenciaController.solicitarMonto()
                    if monto:
                        saldoCuentaOrigen = cuentaOrigen[3]
                        topeCuentaOrigen = cuentaOrigen[7]
                        id_cuentaBancariaOrigen = cuentaOrigen[0]
                        if saldoCuentaOrigen >= monto:
                            if topeCuentaOrigen >= monto:
                                saldoCuentaOrigen = float(saldoCuentaOrigen)
                                saldoCuentaOrigen = saldoCuentaOrigen - monto
                                topeCuentaOrigen = float(topeCuentaOrigen)
                                topeCuentaOrigen = topeCuentaOrigen - monto
                                saldoCuentaDestino = cuentaBancariaDestino[5]
                                saldoCuentaDestino = float(saldoCuentaDestino)
                                saldoCuentaDestino = saldoCuentaDestino + monto
                                id_cuentaBancariaDestino = cuentaBancariaDestino[0]
                                descripcion = TransferenciaController.obtenerDescripcion()
                                transferencia = CuentaBancariaController.realizarTransferencia(id_cuentaBancariaOrigen, id_cuentaBancariaDestino,saldoCuentaDestino,saldoCuentaOrigen, topeCuentaOrigen)
                                
                                if transferencia:
                                    numeroCuentaDestino = cuentaBancariaDestino[2]
                                    transaccion = TransaccionController.registrarTransferencia(id_cuentaBancariaOrigen, id_cuentaBancariaDestino, monto, descripcion)
                                    if transaccion:
                                        numeroCuentaOrigen = cuentaOrigen[1]
                                        TransaccionController.imprimirReciboTransferencia(numeroCuentaOrigen,numeroCuentaDestino,monto, descripcion)
                            else:
                                print("Tope diario superado.")
                        else:
                            print("Saldo insuficiente.")
            else:
                print("No existe esta cuenta.")
    @staticmethod
    def obtenerNumeroCuenta():
        print("***********************************")
        print("...")
        while True:
            numeroCuenta = input("Digite el número de cuenta de destino: ")
            if numeroCuenta:
                return numeroCuenta
            else:
                print("Por favor digite un número de cuenta valido")
        
        CuentaBancariaDestino = input("Escriba la cuenta de destino: ")
    @staticmethod
    def mostrarCuenta(cuenta):
        numeroCuenta = cuenta[1]
        tipoCuenta = cuenta[2]
        nombres = cuenta[3]
        apellidos = cuenta[4]
        titular = nombres + " " + apellidos
        
        print("***********************************")
        print("...")
        print("Numero de cuenta: ", numeroCuenta)
        print("Tipo de cuenta: ", tipoCuenta)
        print("titular: ", titular)
        print("***********************************")
        print("...")
        print("desea continuar?")
        print("1. continuar")
        print("2. cancelar")
        pregunta = input("Desea continuar?")
        pregunta = int(pregunta)
        if pregunta == 1:
            return True
        else:
            print("Gracias por visitarnos, ¡Vuelve pronto!")
        
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
            if tarjeta:
                tipoTarjeta = tarjeta[3]
                if tipoTarjeta == 'DEBITO':
                    cuenta = CuentaBancariaController.consultarCuentaConTarjeta(tarjeta)
                    tipoCuenta = cuenta[4]
                    if tipoCuenta == 'CORRIENTE':
                        opcion = TransferenciaController.menuTransferencias()
                        TransferenciaController.opcionMenu(opcion, cuenta)
                    else:
                        print("***********************************")
                        print("...")
                        print('En esta opcion solamente puede realizar transferencias desde cuentas corriente')
                else:
                    print("***********************************")
                    print("...")
                    print("Su tarjeta es de Credito, para realizar avances seleccione la opción de realizar avances.")
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
                        opcion = TransferenciaController.menuTransferencias()
                        if opcion:
                            TransferenciaController.opcionMenu(opcion, cuenta)
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
                        opcion = TransferenciaController.menuTransferencias()
                        if opcion:
                            TransferenciaController.opcionMenu(opcion, cuenta)
                else:
                    print("***********************************")
                    print("...")
                    print('En esta opcion solamente puede realizar retiros de Ahorro a la mano')