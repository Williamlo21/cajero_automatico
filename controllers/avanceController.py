from controllers.tarjetaController import TarjetaController
from controllers.transaccionController import TransaccionController
class AvanceController():
    
    @staticmethod
    def principal():
        tarjeta = TarjetaController.insertarTarjeta()
        if tarjeta:
            tipoTarjeta = tarjeta[3]
            if tipoTarjeta == 'CREDITO':
                opcion = TransaccionController.seleccionaMontoConCuenta()
                resultado = TransaccionController.opcionMonto(opcion, tarjeta)
                if resultado:
                    cuenta = resultado[0]
                    monto = resultado[1]
                    TransaccionController.hacerAvance(cuenta, monto)
                
            else:
                print("***********************************")
                print("...")
                print("Su tarjeta es Debito, para realizar retiros seleccione la opción de realizar retiro.")
    
        
    @staticmethod
    def menuAvance():
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
        # Retiro().opcionRetiro(opcion)