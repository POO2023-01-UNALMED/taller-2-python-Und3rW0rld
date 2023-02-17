class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self, color):
        color = color.lower()
        if color in ["rojo", "amarillo", "verde", "negro", "blanco"]:
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cont = 0;
        for i in self.asientos:
            if i != None:
                cont+=1
        return cont
    def verificarIntegridad(self):
        valido = self.registro == self.motor.registro
        if(valido):
            for asiento in self.asientos:
                if asiento!= None:
                    if(asiento.registro!= self.registro):
                        valido = False
                        break
        return "Auto original" if valido else "Las piezas no son originales"
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        tipo = tipo.lower()
        if(tipo in ["electrico", "gasolina"]):
            self.tipo = tipo