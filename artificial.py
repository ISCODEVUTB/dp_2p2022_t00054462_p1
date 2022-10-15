from personaje_builder import PersonajeBuilder
from enumerations import Genre

class Artificial(PersonajeBuilder):

    def __init__(self, alias = "",real_name = "", height = 0.0, weight = 0.0,genre = Genre.NONE, characterizations = None, liga = "", enemigo = None) -> None:
        self.alias = alias
        self.real_name = real_name
        self.height = height
        self.weight = weight
        self.genre = genre
        self.characterizations = characterizations
        self.liga = liga
        self.enemigo = enemigo

    def build_move(self):
        self.personaje.set_move(move = "move -> Artificial")
    
    def build_jump(self):
        self.personaje.set_jump(jump = "jump -> Artificial")
    
    def build_attack(self):
        self.personaje.set_attack(attack = "attack -> Artificial")

    def build_defend(self):
        self.personaje.set_defend(defend = "defend -> Artificial")