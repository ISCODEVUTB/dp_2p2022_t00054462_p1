from abc import abstractmethod
from caracterizacion import Caracterizacion
from enumerations import Genre


class Personaje():
    alias: str
    real_name: str
    genre: Genre
    height: float
    weight: float
    characterizations = []
    liga = ''
    enemigo = None


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

    def speak(self, idiom: str, script: str) -> str:
        """
        Recibe el nombre del idioma en que hablara el personaje y lo que debe decir.
        """
        return "El personaje dice: " + script + " en el idioma " + idiom

    @abstractmethod
    def move(self) -> str:
        pass

    @abstractmethod
    def jump(self) -> str:
        pass

    @abstractmethod
    def attack(self) -> str:
        pass

    @abstractmethod
    def defend(self) -> str:
        pass

    def to_string(self) -> str:
        return f'alias: {self.alias}, real_name: {self.real_name}, genre: {self.genre}, height: {self.height}, weight: {self.weight}'