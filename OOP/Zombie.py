from Enemigo import *


class Zombie(Enemigo):
    def _intit_(self, puntos_energia=10, ataque=1):
        super()._intit_(tipo_enemigo= 'Zombie', puntos_energia=puntos_energia, ataque=ataque)

        def habla(self):
            print("*Hummmmm...*")

        def propagar_enfermedad(self):
            print("El zombie esta tratanda de propagar la enfermdad!!")
            