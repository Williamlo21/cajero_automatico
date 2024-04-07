from controllers.tarjetaController import TarjetaController
from controllers.transaccionController import TransaccionController
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
            if confirmarTarjeta:
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
        elif opcion == 2:
            print("cuenta de corriente")
        elif opcion == 3:
            print("nequi")
        elif opcion == 4:
            print("a la mano")
        elif opcion == 5:
            print("Gracias por visitarnos, ¡Vuelve pronto!")
        else:
            print("Por favor digite una opción valida")
            Retiro().tipoDeRetiro()


            
