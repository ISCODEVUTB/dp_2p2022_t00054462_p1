import unittest
from humano import Humano
from superhumano import Superhumano
from debilidades import Debilidades
from personalidad import Personalidad
from enumerations import Genre, Morality, Identity, Personality, Character

class TestNewLigue(unittest.TestCase):

    personaje_superhumano = Superhumano("La viuda negra", "Natasha", 1.72, 68.4, Genre.FEMALE, Morality.HERO, Identity.PUBLIC)
    personaje_humano = Humano("El joker", "Unknown", 1.78, 73.0, Genre.MALE, "Blanco", "Marrones", "Negro")
    debilidad = Debilidades("aragnofobia", "trauma de niñez", 2.4, "arañas")
    personalidad = Personalidad("Arrogancia", "De nacimiento", Personality.EXTROVERT, Character.IMPASSIONED)


    def test_add_debilidad(self):
        self.assertTrue(self.personaje_superhumano.add(self.debilidad))

    def test_enemigo_superhumano(self):
        self.assertTrue(self.personaje_humano.enemigo(self.personaje_superhumano))

    def test_add_personalidad(self):
        self.assertTrue(self.personaje_humano.add(self.personalidad))


if __name__ == '__main__':
    unittest.main()