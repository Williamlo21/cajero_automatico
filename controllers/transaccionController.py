from models.cuentaBancaria import CuentaBancaria
from models.transaccion import Transaccion
from datetime import datetime
import decimal

class TransaccionController():
    def seleccionaMonto(self, tarjeta):
        print("***********************************")
        print("...")
        opciones = {
            "1" : "$20.000",
            "2" : "$50.000",
            "3" : "$100.000",
            "4" : "$200.000",
            "5" : "$500.000",
            "6" : "Otro",
        }
        
        for clave, valor in opciones.items():
            print(clave + ": " + valor)
        opcion = input("Digite el monto a retirar: ")
        TransaccionController().opcionMonto(opcion, tarjeta)
        
    def opcionMonto(self, opcion, tarjeta):
        opcion = int(opcion)
        if opcion == 1:
            monto = 20000
            TransaccionController().verificarMonto(monto, tarjeta)
        elif opcion == 2:
            monto = 50000
            TransaccionController().verificarMonto(monto, tarjeta)
        elif opcion == 3:
            monto = 100000
            TransaccionController().verificarMonto(monto, tarjeta)
        elif opcion == 4:
            monto = 200000
            TransaccionController().verificarMonto(monto, tarjeta)
        elif opcion == 5:
            monto = 500000
            TransaccionController().verificarMonto(monto, tarjeta)
        elif opcion == 6:
            monto = input("Digite el monto que desea retirar: ")
            TransaccionController().verificarMonto(monto, tarjeta)
        else:
            print("Por favor digite una opción valida")
            TransaccionController().seleccionaMonto(tarjeta)
            
    def verificarMonto(self, monto, tarjeta):
        cuenta = CuentaBancaria.consultarCuenta(tarjeta)

        saldo = cuenta[3]
        tope = cuenta[7]
        monto = decimal.Decimal(monto)
        if saldo >= monto:
            if tope >= monto:
                retiro = CuentaBancaria.realizarRetiro(cuenta, monto)
                if retiro:
                    print("***********************************")
                    print("...")
                    print("Retire el dinero")
                    print("***Billetes***")
                    transaccion = Transaccion.registrarRetiro(cuenta, monto)
                    if transaccion:
                        print("***********************************")
                        print("...")
                        print("***Recibo***")
                        cuentaActualizada = CuentaBancaria.consultarCuenta(cuenta)
                        dt = datetime.now()
                        # ahora creamos la variable con la fecha de hoy
                        fecha = dt
                        print("Fecha del retiro:", fecha)
                        print("Cuenta de retiro:", cuentaActualizada[1]) 
                        print("Monto retirado:", monto)
                        print("Restante de tope:", cuentaActualizada[6])  
                        print("***********************************")
                        print("***Gracias por preferirnos***")
            else:
                print("***********************************")
                print("Tope diario superado.")
        else:
            print("***********************************")
            print("Saldo insuficiente.")
        