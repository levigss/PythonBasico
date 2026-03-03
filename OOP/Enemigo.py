class Enemigo:
    # 1. Corrección del nombre: __init__ (doble guion bajo)
    def __init__(self, tipo_enemigo, puntos_energia=10, ataque=1):
        self.tipo_enemigo = tipo_enemigo
        # 2. Usamos los nombres exactos que pide tu main.py
        self.puntos_energia = puntos_energia
        self.ataque = ataque

    def get_tipo_enemigo(self):
        return self.tipo_enemigo
    
    def habla(self):
        print(f"Yo soy {self.tipo_enemigo}. ¡Preparado para pelear!!")

    def camina(self):
        print(f"{self.tipo_enemigo} se mueve cerca de ti!!!")

    def atacar(self):
        print(f"{self.tipo_enemigo} ataca con {self.ataque} de daño!!")

    def ataque_especial(self):
        print("Enemigo no tiene ataque especial")