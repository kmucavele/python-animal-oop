from abc import abstractmethod
from datetime import date

from animal_definitions.animal import Animal
from animal_definitions.diet import Diet
from animal_definitions.gender import Gender


class FlyingAnimals(Animal):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, lays_eggs: bool):
        super().__init__(name, gender, species, diet, birthday)
        self.__lays_eggs = lays_eggs

    @property
    def lays_eggs(self):
        return self.__lays_eggs

    def fly(self) -> None:
        print(f"{self._action_str_prefix()} flying")

    @abstractmethod
    def clean_wings(self) -> None:
        pass
