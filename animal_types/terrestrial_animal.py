from abc import abstractmethod
from datetime import date

from animal_definitions.animal import Animal
from animal_definitions.diet import Diet
from animal_definitions.gender import Gender


class TerrestrialAnimal(Animal):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, legs: int,  has_tail: bool):
        super().__init__(name, gender, species, diet, birthday)
        self.__has_tail = has_tail
        self.__legs = legs

    @property
    def legs(self) -> int:
        return self.__legs

    @legs.setter
    def legs(self, numb_of_legs: int):
        self.__legs = numb_of_legs

    @property
    def has_tail(self) -> int:
        return self.__has_tail

    @has_tail.setter
    def has_tail(self, has_tail: bool):
        self.__has_tail = has_tail

    @abstractmethod
    def run(self):
        pass
