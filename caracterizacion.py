from abc import ABC, abstractmethod

class Caracterizacion(ABC):
    """
    Es una clase abstracta que tiene como subclases de Poderes, Habilidades, Debilidades, Armas, Personalidad.
    """
    name: str
    origen: str

    def __init__(self, name: str, origen: str):
        self.name = name
        self.origen = origen

    def get_name(self) -> str:
        return self.name

    def set_name(self, name:str) -> None:
        self.name = name

    def get_origen(self) -> str:
        return self.origen

    def set_origen(self, origen: str) -> None:
        self.origen = origen

    @abstractmethod
    def change_power(self) -> str:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass
