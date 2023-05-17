class Arco:
    def __init__(self,origen,destino,peso):
        self.origen=origen
        self.destino=destino
        self.peso=int(peso)

    def __str__(self):
        return f'origen = {self.origen.nombre}, destino = {self.destino.nombre}, peso = {self.peso}'