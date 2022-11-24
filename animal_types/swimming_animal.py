from abc import ABC, abstractmethod
from datetime import date

from animal_definitions.animal import Animal
from animal_definitions.diet import Diet
from animal_definitions.gender import Gender


class SwimmingAnimals(Animal):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date):
        super().__init__(name, gender, species, diet, birthday)

    def swim(self) -> None:
        print(self._action_str_prefix() + " swimming")

    @abstractmethod
    def move(self) -> None:
        pass
