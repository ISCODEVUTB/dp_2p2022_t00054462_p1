from personaje import Personaje
from enumerations import Genre
from abc import abstractmethod

class PersonajeBuilder:
    personaje: Personaje
    alias: str
    real_name: str
    genre: Genre
    height: float
    weight: float
    characterizations = []
    liga = ''
    enemigo = None

    def get_personaje(self) -> Personaje:
        return self.personaje

    def crete_new_personaje(self):
        self.personaje = Personaje(self.alias,self.real_name, self.height, self.weight, self.genre, self.characterizations, self.liga, self.enemigo)

    @abstractmethod
    def build_move():
        pass
    
    @abstractmethod
    def build_jump():
        pass
    
    @abstractmethod
    def build_attack():
        pass

    @abstractmethod
    def build_defend():
        pass
