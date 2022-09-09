from caracterizacion import Caracterizacion
from personaje import Personaje
from enumerations import Morality, Identity, Genre


class Superhumano(Personaje):
    morality: Morality
    identity: Identity

    def __init__(self, alias: str, real_name: str, height: float, weight: float, genre: Genre, morality: Morality, identity: Identity, characterizations = [], liga: str = '', enemigo=None):
        super().__init__(alias, real_name, height, weight, genre)
        self.morality = morality
        self.identity = identity
    
    def get_morality(self) -> Morality:
        return self.morality

    def set_morality(self, morality: Morality) -> None:
        self.morality = morality

    def get_identity(self) -> Identity:
        return self.identity

    def set_identity(self, identity: Identity) -> None:
        self.identity = identity

    def move(self) -> str:
        return f'move -> Superhumano'

    def jump(self) -> str:
        return f'jump -> Superhumano'

    def attack(self) -> str:
        return f'attack -> Superhumano'

    def defend(self) -> str:
        return f'defend -> Superhumano'

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
        return personaje_info + f', morality: {self.morality}, identity: {self.identity}'

    