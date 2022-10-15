import unittest
from armas import Armas
from humano import Humano
from alien import Alien
from artificial import Artificial
from superhumano import Superhumano
from debilidades import Debilidades
from personalidad import Personalidad
from enumerations import Genre, Morality, Identity, Personality, Character
from personaje_director import PersonajeDirector

class TestNewLigue(unittest.TestCase):

    superhumano_builder = Superhumano("La viuda negra", "Natasha", 1.72, 68.4, Genre.FEMALE, Morality.HERO, Identity.PUBLIC)
    humano_builder = Humano("El joker", "Unknown", 1.78, 73.0, Genre.MALE, "Blanco", "Marrones", "Negro")
    alien_builder = Alien("Quick Silver", "Pietro", "1.84", "85", Genre.MALE, "Jupiter")
    artificial_builder = Artificial("Ultron", "Ultron", "1.90", "80", Genre.MALE, "Tony Stark" )
    
    debilidad = Debilidades("aragnofobia", "trauma de niñez", 2.4, "arañas")
    personalidad = Personalidad("arrogancia", "De nacimiento", Personality.EXTROVERT, Character.IMPASSIONED)
    armas = Armas("Martillo de thor", "Fue un regalo de loki", "0.90")


    #Test Build humano
    def test_build_humano(self):
        personaje_director = PersonajeDirector()
        personaje_director.set_personaje_builder(self.humano_builder)
        personaje_director.construct_personaje()
        completed_humano = personaje_director.get_personaje()

        self.assertEqual([
            completed_humano.move,
            completed_humano.attack, 
            completed_humano.defend,
            completed_humano.jump
        ],
        [
            "move -> Humano",
            "attack -> Humano",
            "defend -> Humano",
            "jump -> Humano"

        ])

    #Test Build superhumano
    def test_build_superhumano(self):
        personaje_director = PersonajeDirector()
        personaje_director.set_personaje_builder(self.superhumano_builder)
        personaje_director.construct_personaje()
        completed_superhumano = personaje_director.get_personaje()

        self.assertEqual([
            completed_superhumano.move,
            completed_superhumano.attack, 
            completed_superhumano.defend,
            completed_superhumano.jump
        ],
        [
            "move -> Superhumano",
            "attack -> Superhumano",
            "defend -> Superhumano",
            "jump -> Superhumano"

        ])

    #Test Build alien
    def test_build_alien(self):
        personaje_director = PersonajeDirector()
        personaje_director.set_personaje_builder(self.alien_builder)
        personaje_director.construct_personaje()
        completed_alien = personaje_director.get_personaje()

        self.assertEqual([
            completed_alien.move,
            completed_alien.attack, 
            completed_alien.defend,
            completed_alien.jump
        ],
        [
            "move -> Alien",
            "attack -> Alien",
            "defend -> Alien",
            "jump -> Alien"

        ])

    #Test Build artificial
    def test_build_artificial(self):
        personaje_director = PersonajeDirector()
        personaje_director.set_personaje_builder(self.artificial_builder)
        personaje_director.construct_personaje()
        completed_artificial = personaje_director.get_personaje()

        self.assertEqual([
            completed_artificial.move,
            completed_artificial.attack, 
            completed_artificial.defend,
            completed_artificial.jump
        ],
        [
            "move -> Artificial",
            "attack -> Artificial",
            "defend -> Artificial",
            "jump -> Artificial"

        ])

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

    # Test to_string methods
    def test_to_string(self):
        personaje_director = PersonajeDirector()
        personaje_director.set_personaje_builder(self.superhumano_builder)
        personaje_director.construct_personaje()
        completed_superhumano = personaje_director.get_personaje()
        wait_result = f'alias: La viuda negra, real_name: Natasha, genre: {Genre.FEMALE}, height: 1.72, weight: 68.4'
        self.assertEqual(completed_superhumano.to_string(), wait_result)



if __name__ == '__main__':
    unittest.main()