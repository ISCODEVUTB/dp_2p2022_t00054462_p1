from caracterizacion import Caracterizacion
from personaje import Personaje
from enumerations import Genre


class Alien(Personaje):
    planet: str

    def __init__(self, alias: str, real_name: str, height: float, weight: float, genre: Genre, planet: str, characterizations = [], liga: str = '', enemigo=None):
        super().__init__(alias, real_name, type, height, weight, genre)
        self.planet = planet

    def get_planet(self) -> str:
        return self.planet

    def set_planet(self, planet: str) -> None:
        self.planet = planet

    def back_home(self):
        return f'{self.alias} va de regreso a {self.planet}'

    def move(self) -> str:
        return f'move -> Alien'

    def jump(self) -> str:
        return f'jump -> Alien'

    def attack(self) -> str:
        return f'attack -> Alien'

    def defend(self) -> str:
        return f'defend -> Alien'

    def add(self, characterization: Caracterizacion) -> bool:
        try:
            if(isinstance(characterization, Caracterizacion)):
                self.characterizations.append(characterization)
                return True
            else:
                raise ValueError
        except Exception:
            return False

    def liga(self, liga:str) -> bool:
        try:
            self.liga = liga
            return bool
        except Exception:
            return False

    def enemigo(self, enemigo: Personaje):
        try:
            if(isinstance(enemigo, Personaje)):
                self.characterizations.append(enemigo)
                return True
            else:
                raise ValueError
        except Exception:
            return False

    def to_string(self) -> str:
        personaje_info = super().to_string()
        return personaje_info + f', planet: {self.planet}'