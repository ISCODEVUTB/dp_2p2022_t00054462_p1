from caracterizacion import Caracterizacion
from personaje import Personaje
from enumerations import MaritalStatus, Genre
from IFicha import IFicha


class Humano(Personaje, IFicha):
    race: str
    color_eye: str
    color_hair: str

    def __init__(self, alias: str, real_name: str, height: float, weight: float, genre: Genre, race: str, color_eye:str, color_hair: str, characterizations = [], liga: str = '', enemigo=None):
        super().__init__(alias, real_name, height, weight, genre, characterizations, liga, enemigo)
        self.race = race
        self.color_eye = color_eye
        self.color_hair= color_hair

    def get_race(self) -> str:
        return self.race

    def set_race(self, race:str) -> None:
        self.race = race

    def get_color_eye(self) -> str:
        return self.color_eye

    def set_color_eye(self, color_eye:str) -> None:
        self.color_eye = color_eye

    def get_color_hair(self) -> str:
        return self.color_hair

    def set_color_hair(self, color_hair:str) -> None:
        self.color_hair = color_hair
  
    def move(self) -> str:
        return f'move -> Humano'

    def jump(self) -> str:
        return f'jump -> Humano'

    def attack(self) -> str:
        return f'attack -> Humano'

    def defend(self) -> str:
        return f'defend -> Humano'

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
        return personaje_info + f', race: {self.race}, color eye: {self.color_eye}, color hair: {self.color_hair}'
        

