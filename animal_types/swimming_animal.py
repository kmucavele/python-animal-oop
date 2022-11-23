from abc import ABC, abstractmethod
from datetime import date

from animal_definitions.animal import Animal
from animal_definitions.diet import Diet
from animal_definitions.gender import Gender


class SwimmingAnimals(Animal, ABC):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, is_alive: bool):
        super().__init__(name, gender, species, diet, birthday, is_alive)

    def swim(self) -> None:
        print(self._action_str_prefix() + " swimming")

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def defend(self) -> None:
        pass

    @abstractmethod
    def make_sound(self) -> None:
        pass
