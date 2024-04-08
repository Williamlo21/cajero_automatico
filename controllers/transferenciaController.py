
class TransferenciaController():
    
    @staticmethod
    def principal():
        print("***********************************")
        print("...")
        opcion = TransferenciaController.menuTransferencias()
        
    @staticmethod
    def menuTransferencias():
        opciones = {
            "1" : "Cuenta inscrita.",
            "2" : "Cuenta no inscrita.",
        }
        
        for clave, valor in opciones.items():
            print(clave + ": " + valor)
        opcion = input("Digite la opción: ")
        return opcion