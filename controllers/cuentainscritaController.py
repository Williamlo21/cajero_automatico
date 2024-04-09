
from models.cuentasInscritas import CuentaInscrita
class CuentaInscritaController():
    @staticmethod
    def consultarCuentasInscritas(cuentaOrigen):
        cuentasInscritas = CuentaInscrita.consultarCuentasInscritas(cuentaOrigen)
        if cuentasInscritas:
            return cuentasInscritas
    @staticmethod
    def mostrarCuentasInscritas(cuentasInscritas):
        print("***********************************")
        print("...")
        print("Cuentas inscritas")
        opciones = {}
        i = 1
        for cuenta in cuentasInscritas:
            id = cuenta[0]
            numero_cuenta = cuenta[1]
            tipo_cuenta = cuenta[2]
            nombres = cuenta[3]
            apellidos = cuenta[4]
            saldo = cuenta[5]
            print("------------------------------------")
            print("Cuenta No.", i)
            
            print("Número de cuenta:", numero_cuenta)
            print("Tipo de cuenta:", tipo_cuenta)
            print("Nombres:", nombres)
            print("Apellidos:", apellidos)
            print("------------------------------------")
            opcion = str(i)  # Podrías usar el número de cuenta como opción si lo deseas
            i = i+1
            descripcion_cuenta = f"{id} - {numero_cuenta} - {tipo_cuenta} - {nombres} - {apellidos} - {saldo}"
            opciones[opcion] = descripcion_cuenta
        
        
        return opciones
    @staticmethod
    def escogerCuentaInscrita(opciones):
        print("***********************************")
        print("...")
        numeroOpciones = len(opciones)
        cuentaBancariaDestino_valida = False
        while cuentaBancariaDestino_valida == False:
        
            cuentaBancariaDestino = input("Escoja la cuenta de destino: ")
            cuentaBancariaDestino = int(cuentaBancariaDestino)
            if cuentaBancariaDestino <= 0  or cuentaBancariaDestino > numeroOpciones :
                print("Opicion invalida")
            else:
                return cuentaBancariaDestino
