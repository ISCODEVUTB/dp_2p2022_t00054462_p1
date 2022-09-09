from caracterizacion import Caracterizacion
from personaje import Personaje
from enumerations import Genre


class Artificial(Personaje):
    creator:str

    def __init__(self, alias: str, real_name: str, height: float, weight: float, genre: Genre, creator:str, characterizations = [], liga: str = '', enemigo=None):
        super().__init__(alias, real_name, height, weight, genre)
        self.creator = creator

    def get_creator(self) -> str:
        return self.creator

    def set_creator(self, creator:str) -> None:
        self.creator = creator

    def move(self) -> str:
        return f'move -> Artificial'

    def jump(self) -> str:
        return f'jump -> Artificial'

    def attack(self) -> str:
        return f'attack -> Artificial'

    def defend(self) -> str:
        return f'defend -> Artificial'

    def add(self, characterizations: Caracterizacion) -> bool:
        try:
            self.characterizations.append(characterizations)
            return bool
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
            self.enemigo = enemigo
            return bool
        except Exception:
            return False

    def to_string(self) -> str:
        personaje_info = super().to_string()
        return personaje_info + f', creator: {self.creator}'
