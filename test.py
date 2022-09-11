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
    personalidad = Personalidad("arrogancia", "De nacimiento", Personality.EXTROVERT, Character.IMPASSIONED)
    armas = Armas("Martillo de thor", "Fue un regalo de loki", "0.90")

    # Tests Clase superhumano
    def test_add_superhumano(self):
        self.assertTrue(self.personaje_superhumano.add(self.debilidad))

    def test_enemigo_superhumano(self):
        self.assertTrue(self.personaje_superhumano.enemigo(self.personaje_humano))

    def test_liga_superhumano(self):
        self.assertTrue(self.personaje_superhumano.liga("Los vengadores"))

    def test_speak_superhumano(self):
        result = self.personaje_superhumano.speak('español', 'yo los protegere')
        self.assertEqual(result, 'El personaje dice: yo los protegere en el idioma español')

    def test_move_superhumano(self):
        self.assertEqual(self.personaje_superhumano.move(), 'move -> Superhumano')

    def test_jump_superhumano(self):
        self.assertEqual(self.personaje_superhumano.jump(), 'jump -> Superhumano')

    def test_attack_superhumano(self):
        self.assertEqual(self.personaje_superhumano.attack(), 'attack -> Superhumano')

    def test_defend_superhumano(self):
        self.assertEqual(self.personaje_superhumano.defend(), 'defend -> Superhumano')

    # Tests clase humano
    def test_enemigo_humano(self):
        self.assertTrue(self.personaje_humano.enemigo(self.personaje_superhumano))

    def test_add_humano(self):
        self.assertTrue(self.personaje_humano.add(self.personalidad))

    def test_liga_humano(self):
        self.assertTrue(self.personaje_humano.liga("Starlord group"))

    def test_speak_humano(self):
        result = self.personaje_humano.speak('español', 'este es mi planeta')
        self.assertEqual(result, 'El personaje dice: este es mi planeta en el idioma español')

    def test_move_humano(self):
        self.assertEqual(self.personaje_humano.move(), 'move -> Humano')

    def test_jump_humano(self):
        self.assertEqual(self.personaje_humano.jump(), 'jump -> Humano')

    def test_attack_humano(self):
        self.assertEqual(self.personaje_humano.attack(), 'attack -> Humano')

    def test_defend_humano(self):
        self.assertEqual(self.personaje_humano.defend(), 'defend -> Humano')

    # Tests clase Alien
    def test_add_alien(self):
        self.assertTrue(self.personaje_alien.add(self.armas))

    def test_enemigo_alien(self):
        self.assertTrue(self.personaje_alien.enemigo(self.personaje_artificial))

    def test_liga_alien(self):
        self.assertTrue(self.personaje_alien.liga("Los 4 fantasticos"))

    def test_speak_alien(self):
        result = self.personaje_alien.speak('español', 'vengo en paz')
        self.assertEqual(result, 'El personaje dice: vengo en paz en el idioma español')

    def test_move_alien(self):
        self.assertEqual(self.personaje_alien.move(), 'move -> Alien')

    def test_jump_alien(self):
        self.assertEqual(self.personaje_alien.jump(), 'jump -> Alien')

    def test_attack_alien(self):
        self.assertEqual(self.personaje_alien.attack(), 'attack -> Alien')

    def test_defend_alien(self):
        self.assertEqual(self.personaje_alien.defend(), 'defend -> Alien')

    # Tests clase Artificial
    def test_add_artificial(self):
        self.assertTrue(self.personaje_artificial.add(self.personalidad))

    def test_enemigo_artificial(self):
        self.assertTrue(self.personaje_artificial.enemigo(self.personaje_alien))

    def test_liga_artificial(self):
        self.assertTrue(self.personaje_artificial.liga("Los vengadores"))

    def test_speak_artificial(self):
        result = self.personaje_artificial.speak('español', 'estoy vivo')
        self.assertEqual(result, 'El personaje dice: estoy vivo en el idioma español')

    def test_move_artificial(self):
        self.assertEqual(self.personaje_artificial.move(), 'move -> Artificial')

    def test_jump_artificial(self):
        self.assertEqual(self.personaje_artificial.jump(), 'jump -> Artificial')

    def test_attack_artificial(self):
        self.assertEqual(self.personaje_artificial.attack(), 'attack -> Artificial')

    def test_defend_artificial(self):
        self.assertEqual(self.personaje_artificial.defend(), 'defend -> Artificial')

    
    #Tests Caracterizaciones methods

    def test_armas(self):
        result = self.armas.change_power()
        self.assertEqual(result, 'Increase power for Martillo de thor')

    def test_debilidades(self):
        result = self.debilidad.change_power()
        self.assertEqual(result, 'Decrease power for aragnofobia')

    def test_personalidad(self):
        result = self.personalidad.change_power()
        self.assertEqual(result, 'Decrease power for arrogancia')


if __name__ == '__main__':
    unittest.main()