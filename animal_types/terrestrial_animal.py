from abc import abstractmethod,
from datetime import date

from animal_definitions.animal import Animal
from animal_definitions.diet import Diet
from animal_definitions.gender import Gender


class TerrestrialAnimal(Animal):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, is_alive: bool,
                 legs: int):
        super().__init__(name, gender, species, diet, birthday, is_alive)
        self.__legs = legs

    @abstractmethod
    def run(self):
        pass



