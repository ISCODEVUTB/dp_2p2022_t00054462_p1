from abc import abstractmethod
from abc import ABCMeta


class IFicha(metaclass=ABCMeta):

    @abstractmethod
    def add(self):
        """
        Este método recibirá por parámetro un tipo de caracterización
        """
        pass

    @abstractmethod
    def liga(self):
        """
        Es un método que adiciona a la liga o grupo que pertenece el personaje.
        """
        pass

    @abstractmethod
    def enemigo(self):
        """
        Es un método que adiciona un personaje, el cual es el enemigo de dicho personaje creado
        """
        pass