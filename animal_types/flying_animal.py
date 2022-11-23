from abc import ABC, abstractmethod
from datetime import date

from animal_definitions.animal import Animal
from animal_definitions.diet import Diet
from animal_definitions.gender import Gender


class FlyingAnimals(Animal, ABC):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, is_alive: bool,
                 lays_eggs: bool):
        super().__init__(name, gender, species, diet, birthday, is_alive)
        self.__lays_eggs = lays_eggs

    def fly(self) -> None:
        print(self._action_str_prefix() + " flying")

    @abstractmethod
    def play(self) -> str:
        pass

    @abstractmethod
    def defend(self):
        pass

    @abstractmethod
    def make_sound(self) -> str:
        pass
