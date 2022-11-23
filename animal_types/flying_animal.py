from abc import ABC, abstractmethod
from datetime import date

from animal_definitions.animal import Animal
from animal_definitions.diet import Diet
from animal_definitions.gender import Gender


class FlyingAnimals(Animal):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, is_alive: bool,
                 lays_eggs: bool):
        super().__init__(name, gender, species, diet, birthday, is_alive)
        self.__lays_eggs = lays_eggs

    def fly(self) -> None:
        print(f"{self._action_str_prefix()} flying")

    @abstractmethod
    def clean_wings(self) -> None:
        pass


if __name__ == '__main__':
    fly_an = FlyingAnimals(None, None, None, None, None, None, None)
