from models.tarjeta import Tarjeta
class TarjetaController():
    @staticmethod
    def insertarTarjeta():
        print("***********************************")
        print("...")
        tarjeta = input("Por favor inserte su tarjeta: ")
        tarjetaExiste = Tarjeta()
        confirmarTarjeta = tarjetaExiste.existeTarjeta(tarjeta)
        if confirmarTarjeta:
            claveTarjeta = str(confirmarTarjeta[6])
            clave = input("Ingrese la clave: ")
            if clave == claveTarjeta:
            
                return confirmarTarjeta
            else:
                print("Clave invalida.")