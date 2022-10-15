from IFicha import IFicha
from caracterizacion import Caracterizacion
from enumerations import Genre

class Personaje(IFicha):
    alias: str
    real_name: str
    genre: Genre
    height: float
    weight: float
    characterizations = []
    liga = ''
    enemigo = None

    move: str
    jump: str
    attack: str
    defend: str

    def __init__(self, alias:str, real_name:str, height:float, weight:float, genre: Genre, characterizations = [], liga: str = '', enemigo = None):
        self.alias = alias
        self.real_name = real_name
        self.height = height
        self.weight = weight
        self.genre = genre

    def get_alias(self) -> str:
        return self.alias

    def set_alias(self, alias:str) -> None:
        self.alias = alias

    def get_real_name(self) -> str:
        return self.real_name

    def set_real_name(self, real_name:str) -> None:
        self.real_name = real_name

    def get_genre(self) -> Genre:
        return self.genre

    def set_genre(self, genre:Genre) -> None:
        self.genre = genre

    def get_height(self) -> float:
        return self.height

    def set_height(self, height:float) -> None:
        self.height = height

    def get_weight(self) -> float:
        return self.weight

    def set_weight(self, weight:float) -> None:
        self.weight = weight

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

    def enemigo(self, enemigo):
        try:
            if(isinstance(enemigo, Personaje)):
                self.characterizations.append(enemigo)
                return True
            else:
                raise ValueError
        except Exception:
            return False

    def set_move(self, move:str) -> str:
        self.move = move

    def set_jump(self, jump: str) -> str:
        self.jump = jump

    def set_attack(self, attack: str) -> str:
        self.attack = attack

    def set_defend(self, defend: str) -> str:
        self.defend = defend

    def to_string(self) -> str:
        return f'alias: {self.alias}, real_name: {self.real_name}, genre: {self.genre}, height: {self.height}, weight: {self.weight}'