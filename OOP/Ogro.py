from Enemigo import *
import random

class Ogro(Enemigo):
    def __init__(self, puntos_energia=20, ataque=3):
        super().__init__(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataque)
        
    # Estos métodos deben estar al mismo nivel que el __init__
    def habla(self):
        print("Ogro aplastar todo!!!")

    def ataque_especial(self):
        print("Ogro ataque especial")
        funciona_ataque_especial = random.random() < 0.20
        if funciona_ataque_especial:
            self.ataque += 4
            print("Ogro se ha enojado e incrementó su ataque por 4!")

