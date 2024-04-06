class Retiro():
    @staticmethod
    def tipoDeRetiro():
        print("***********************************")
        print("...")
        opciones = {
            "1" : "Retiro cuenta de ahorros.",
            "2" : "Retiro cuenta corriente.",
            "3" : "Retiro nequi.",
            "4" : "Retiro ahorro a la mano.",
            "5" : "Salir.",
            "0" : "Atras.",
        }
        
        for clave, valor in opciones.items():
            print(clave + ": " + valor)
        opcion = input("Digite el típo de retiro: ")
