from caracterizacion import Caracterizacion

class Debilidades(Caracterizacion):
    trigger: str
    duration: float

    def __init__(self, name: str, origen: str, duration: float, trigger: str):
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
        return f'Decrease power for {self.name}'

    def to_string(self) -> str:
        caracterizacion_info = super().to_string()
        return caracterizacion_info + f', trigger: {self.trigger}, duration: {self.duration}'
    

    
