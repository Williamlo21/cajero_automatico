from controllers.cuentaBancariaController import CuentaBancariaController
from controllers.tarjetaController import TarjetaController
class ClaveController():
    @staticmethod
    def cambioDeClave():
        opcion = ClaveController.opcionesClave()
        if opcion:
            if opcion == 1:
                tarjeta = TarjetaController.insertarTarjeta()
                if tarjeta:
                    cuenta = CuentaBancariaController.consultarCuentaConTarjeta(tarjeta)
                    if cuenta:
                        numeroCuenta = cuenta[1]
                        cuentaUser = CuentaBancariaController.consultarCuentaUser(numeroCuenta)
                        if cuentaUser:
                            clave = tarjeta[6]
                            confirmar = ClaveController.mostrarDatosCuenta(cuentaUser)
                            if confirmar:
                                nuevaClave = ClaveController.solicitarNuevaClave(clave)
                                if nuevaClave:
                                    numeroTarjeta = tarjeta[1]
                                    cambiarClave = TarjetaController.cambiarClaveTarjeta(nuevaClave, numeroTarjeta)
                                    if cambiarClave:
                                        print("***********************************")
                                        print("...")
                                        print("Clave actualizada con exito")
            if opcion == 2:
                numero_cuenta = input("Ingrese su numero de cuenta: ")
                cuenta = CuentaBancariaController.consultarCuentaSinTarjeta(numero_cuenta)
                if cuenta:
                    numeroCuenta = cuenta[1]
                    cuentaUser = CuentaBancariaController.consultarCuentaUser(numeroCuenta)
                    if cuentaUser:
                        confirmar = ClaveController.mostrarDatosCuenta(cuentaUser)
                        if confirmar:
                            nuevaClave = ClaveController.solicitarNuevaClave(numeroCuenta)
                            if nuevaClave:
                                idCuenta = cuenta[0]
                                cambiarClave = CuentaBancariaController.cambiarNumerocuenta(idCuenta, nuevaClave)
                                if cambiarClave:
                                    print("***********************************")
                                    print("...")
                                    print("Clave actualizada con exito")
                                                                    
    @staticmethod
    def opcionesClave():
        print("***********************************")
        print("...")
        print("1. Con tarjeta.")
        print("2. Bancolombia o Nequi.")
        while True:
            opcion = input("Digite la opción: ")
            opcion = int(opcion)
            if opcion <= 2 and opcion >= 1:
                return opcion
            else:
                print("Digite una opción valida. ")
    @staticmethod
    def mostrarDatosCuenta(cuentaUser):
        numeroCuenta = cuentaUser[1]
        tipoCuenta = cuentaUser[2]
        nombres = cuentaUser[3]
        apellidos = cuentaUser[4]
        print("***********************************")
        print("...")
        print("Numero de cuenta: ", numeroCuenta)
        print("Tipo de cuenta: ", tipoCuenta)
        print("Titular:", nombres, apellidos)
        print("***********************************")
        print("...")
        print("Desea continuar?")
        opcion = input("1. Para continuar: ")

        if opcion:
            opcion = int(opcion)
            if opcion == 1:
                return True
            else:
                print("Gracias por visitarnos, ¡Vuelve pronto!")
    @staticmethod
    def solicitarNuevaClave(clave):
        clave = int(clave)
        print("***********************************")
        print("...")
        nuevaClave = input("Digite la nueva clave: ")
        nuevaClave = int(nuevaClave)
        while nuevaClave == clave:
            print("La clave nueva no puede ser igual que la anterior.")
            nuevaClave = input("Digite la nueva clave: ")
            nuevaClave = int(nuevaClave)
        return nuevaClave
    @staticmethod
    def solicitarNuevaClave(clave):
        clave = int(clave)
        print("***********************************")
        print("...")
        nuevaClave = input("Digite el número de telefono nuevo: ")
        nuevaClave = int(nuevaClave)
        while nuevaClave == clave:
            print("El número de telefono no puede ser igual que la anterior.")
            nuevaClave = input("Digite el número de telefono nuevo:  ")
            nuevaClave = int(nuevaClave)
        return nuevaClave
