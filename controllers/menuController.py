from controllers.retiroController import Retiro
from controllers.avanceController import AvanceController
from controllers.transferenciaController import TransferenciaController
from controllers.serviciosController import ServicioController
from controllers.claveController import ClaveController
class Menu():
    @staticmethod
    def menuPrincipal():
        opciones = {
            "1" : "Realizar retiro.",
            "2" : "Realizar avance.",
            "3" : "Realizar transferencia.",
            "4" : "Pago de servicios.",
            "5" : "Cambio de clave",
            "6" : "Salir",
        }
        
        for clave, valor in opciones.items():
            print(clave + ": " + valor)
        opcion = input("Digite la opción: ")
        Menu().escogerOpcion(opcion)
    
    def escogerOpcion(self, opcion):
        opcion = int(opcion)
        print("***********************************")
        print("Consultando disponibilidad de la opción.")
        print("...")
        if opcion == 1:
            Retiro.tipoDeRetiro()
        elif opcion == 2:
            AvanceController.principal()
        elif opcion == 3:
            TransferenciaController.principal()
        elif opcion == 4:
            ServicioController.comenzarPago()
        elif opcion == 5:
            ClaveController.cambioDeClave()
        elif opcion == 6:
            print("Gracias por visitarnos, ¡Vuelve pronto!")
        else:
            print("Por favor digite una opción valida")
            Menu().menuPrincipal()
    

