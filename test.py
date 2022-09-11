import unittest
from armas import Armas
from humano import Humano
from alien import Alien
from artificial import Artificial
from superhumano import Superhumano
from debilidades import Debilidades
from personalidad import Personalidad
from enumerations import Genre, Morality, Identity, Personality, Character

class TestNewLigue(unittest.TestCase):

    personaje_superhumano = Superhumano("La viuda negra", "Natasha", 1.72, 68.4, Genre.FEMALE, Morality.HERO, Identity.PUBLIC)
    personaje_humano = Humano("El joker", "Unknown", 1.78, 73.0, Genre.MALE, "Blanco", "Marrones", "Negro")
    personaje_alien = Alien("Quick Silver", "Pietro", "1.84", "85", Genre.MALE, "Jupiter")
    personaje_artificial = Artificial("Ultron", "Ultron", "1.90", "80", Genre.MALE, "Tony Stark" )
    
    debilidad = Debilidades("aragnofobia", "trauma de niñez", 2.4, "arañas")
    personalidad = Personalidad("Arrogancia", "De nacimiento", Personality.EXTROVERT, Character.IMPASSIONED)
    armas = Armas("Martillo de thor", "Fue un regalo de loki", "0.90")

    # Tests Clase superhumano
    def test_add_superhumano(self):
        self.assertTrue(self.personaje_superhumano.add(self.debilidad))

    def test_enemigo_superhumano(self):
        self.assertTrue(self.personaje_superhumano.enemigo(self.personaje_humano))

    # Tests clase humano
    def test_enemigo_humano(self):
        self.assertTrue(self.personaje_humano.enemigo(self.personaje_superhumano))

    def test_add_humano(self):
        self.assertTrue(self.personaje_humano.add(self.personalidad))

    # Tests clase Alien
    def test_add_alien(self):
        self.assertTrue(self.personaje_alien.add(self.armas))

    def test_enemigo_alien(self):
        self.assertTrue(self.personaje_alien.enemigo(self.personaje_artificial))

    # Tests clase Artificial
    def test_add_artificial(self):
        self.assertTrue(self.personaje_artificial.add(self.personalidad))

    def test_enemigo_artificial(self):
        self.assertTrue(self.personaje_artificial.enemigo(self.personaje_alien))



if __name__ == '__main__':
    unittest.main()