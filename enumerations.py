from enum import Enum

class Morality(Enum):
    """
    * Hero
    * Villain
    * Antihero
    * Ambivalent
    """
    HERO = 1
    VILLAIN = 2
    ANTIHEREO = 3
    AMBIVALENT = 4

class Genre(Enum):
    """
    * Male
    * Female
    * No binary
    * None
    """
    MALE = 1
    FEMALE = 2
    NO_BINARY = 3
    NONE = 4

class Identity(Enum):
    """
    * Secret
    * Public
    """
    SECRET = 1
    PUBLIC = 2

class Character(Enum):
    IMPASSIONED = 1
    NERVOUS = 2
    SENTIMENTAL = 3
    EASY_GOING = 4

class Personality(Enum):
    INTROVERT = 0
    EXTROVERT = 1