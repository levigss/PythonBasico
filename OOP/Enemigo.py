class Enemigo:
    tipo_enemigo: str
    puntos_energia : int = 10
    ataque = 1


    def _int_(self, tipo_enemigo, puntos_energia=10, ataque=1):
        self._tipo_enemigo = tipo_enemigo
        self._punto_energia = puntos_energia
        self._ataque = ataque


    def get_tipo_enemigo(self):
        return self._tipo_enemigo
    
    def habla(self):
        print(f"Yo soy {self._tipo_enemigo}. Preaparando para pelear!!")


    def camina(self):
        print(f"{self._tipo_enemigo} se mueve cerca de ti!!!")


    def atacar(self):
        print(f"{self._tipo_enemigo} araca con un {self.ataque} de daño!!")