from controllers.retiroController import Retiro
class Menu():
    @staticmethod
    def menuPrincipal():
        opciones = {
            "1" : "Realizar retiro.",
            "2" : "Realizar avance.",
            "3" : "Realizar transferencia.",
            "4" : "Pago de servicios.",
            "5" : "Salir",
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
            print("Escogiste avance")
        elif opcion == 3:
            print("Realizar transferencia")
        elif opcion == 4:
            print("Escogiste pago")
        elif opcion == 5:
            print("Gracias por visitarnos, ¡Vuelve pronto!")
        else:
            print("Por favor digite una opción valida")
            Menu().menuPrincipal()

