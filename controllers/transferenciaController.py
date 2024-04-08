from controllers.tarjetaController import TarjetaController
from controllers.cuentaBancariaController import CuentaBancariaController
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
    def opcionMenu(opcion):
        opcion = int(opcion)
        if opcion == 1:
            cuentas = 0
        elif opcion == 2:
            print("Cuentas no inscritas")
    @staticmethod
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
            tipoTarjeta = tarjeta[3]
            if tipoTarjeta == 'DEBITO':
                if tarjeta:
                    cuenta = CuentaBancariaController.consultarCuentaConTarjeta(tarjeta)
                    tipoCuenta = cuenta[4]
                    if tipoCuenta == 'AHORRO':
                        opcion = TransferenciaController.menuTransferencias()
                        TransferenciaController.opcionMenu(opcion)
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