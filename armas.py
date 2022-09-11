from caracterizacion import Caracterizacion

class Armas(Caracterizacion):
    striking_power: float
    
    def __init__(self, name: str, origen: str, striking_power: float):
        super().__init__(name, origen)
        self.striking_power = striking_power

    def get_striking_power(self) -> float:
        return self.striking_power

    def set_stricking_powe(self, striking_power: float) -> None:
        self.set_stricking_power = striking_power

    def change_power(self) -> str:
        return f'Increase power of {self.name}'

    def to_string(self) -> str:
        caracterizacion_info = super().to_string() 
        return caracterizacion_info + f', striking_power: {self.striking_power}'
