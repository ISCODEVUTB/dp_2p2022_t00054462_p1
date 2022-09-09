from caracterizacion import Caracterizacion

class Debilidades(Caracterizacion):
    trigger: str
    duration: float

    def __init__(self, name: str, origen: str, duration: str, trigger: float):
        super().__init__(name, origen)
        self.duration = duration
        self.trigger = trigger

    def get_trigger(self) -> str:
        return self.trigger

    def set_trigger(self, trigger: str) -> None:
        self.trigger = trigger

    def get_duration(self) -> float:
        return self.duration

    def set_duration(self, duration: float) -> None:
        self.duration = duration

    def change_power(self) -> str:
        return f'Decrease power'

    def to_string(self) -> str:
        caracyerization_info = super().to_string()
        return caracyerization_info + f', trigger: {self.trigger}, duration: {self.duration}'
    

    
