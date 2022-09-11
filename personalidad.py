from enumerations import Personality, Character
from caracterizacion import Caracterizacion


class Personalidad(Caracterizacion):
    personality_type: Personality
    character: Character
    
    def __init__(self, name: str, origen: str, personality_type: Personality, character: Character):
        super().__init__(name, origen)
        self.personality_type = personality_type
        self.character = character

    def get_personality_type(self) -> Personality:
        return self.personality_type

    def set_personality_type(self, personality_type: Personality) -> None:
        self.personality_type = personality_type

    def get_character(self) -> Character:
        return self.character

    def set_character(self, character: Character) -> None:
        self.character = character

    def change_power(self) -> str:
        return f'Decrease power for {self.name}'

    def to_string(self) -> str:
        caracterizacion_info = super().to_string()
        return caracterizacion_info + f', personality_type: {self.personality_type}, character: {self.character}'


    