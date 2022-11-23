from datetime import date

from animal_definitions.diet import Diet
from animal_definitions.gender import Gender
from animal_types.swimming_animal import SwimmingAnimals


class Octopus(SwimmingAnimals):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, is_alive: bool):
        super().__init__(name, gender, species, diet, birthday, is_alive)
        self.__arms: int = 8

    @property
    def arms(self):
        return self.__arms

    def play(self) -> None:
        print(f"{self._action_str_prefix()} playing catch with a toy")

    def defend(self) -> None:
        print(f"{self._action_str_prefix()} releasing ink")

    def make_sound(self) -> None:
        print("...")

    def camouflage(self) -> None:
        print(f"{self._action_str_prefix()} disguising by camouflage")

    def perform_arm_autonomy(self):
        self.__arms -= 1

    def grow_arm_back(self):
        assert self.__arms < 8, f"{self.name} already has its 8 arms"
        self.__arms += 1


