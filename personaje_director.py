from personaje import Personaje
from personaje_builder import PersonajeBuilder


class PersonajeDirector:
    personaje_builder: PersonajeBuilder

    def set_personaje_builder(self, pb: PersonajeBuilder) -> None:
        self.personaje_builder = pb

    def get_personaje(self) -> Personaje:
        return self.personaje_builder.get_personaje()

    def construct_personaje(self) -> None:
        self.personaje_builder.crete_new_personaje()
        self.personaje_builder.build_move()
        self.personaje_builder.build_jump()
        self.personaje_builder.build_attack()
        self.personaje_builder.build_defend()
