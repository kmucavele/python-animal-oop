from datetime import date

from animal_definitions.diet import Diet
from animal_definitions.gender import Gender
from animal_types.swimming_animal import SwimmingAnimals


class Octopus(SwimmingAnimals):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date):
        super().__init__(name, gender, species, diet, birthday)
        self.__arms: int = 8

    @property
    def arms(self) -> int:
        return self.__arms

    def play(self) -> None:
        print(f"{self._action_str_prefix()} playing catch with a toy")

    def defend(self) -> None:
        print(f"{self._action_str_prefix()} releasing ink and looking for a place to hide")

    def make_sound(self) -> None:
        print("...")

    def move(self) -> None:
        print(f"{self._action_str_prefix()} walking with its {self.__arms} arms")

    def camouflage(self) -> None:
        print(f"{self._action_str_prefix()} disguising by camouflage")

    def perform_arm_autonomy(self) -> None:
        self.__arms -= 1

    def grow_arm_back(self) -> None:
        assert self.__arms < 8, f"{self.name} already has its 8 arms"
        self.__arms += 1
