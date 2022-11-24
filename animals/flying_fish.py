from datetime import date

from animal_definitions.diet import Diet
from animal_definitions.gender import Gender
from animal_types.flying_animal import FlyingAnimals
from animal_types.swimming_animal import SwimmingAnimals


class FlyingFish(FlyingAnimals, SwimmingAnimals):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date):
        super().__init__(name, gender, species, diet, birthday, True)

    def fly(self) -> None:
        self.__jump()
        print(f"and glides")

    def move(self) -> None:
        pass

    def play(self) -> None:
        print(f"{self._action_str_prefix()} practicing gliding")

    def defend(self) -> None:
        print(f"{self.name} ({self.species}) was eaten")
        self.is_alive = False

    def make_sound(self) -> None:
        print(f"{self.name}: 'Blub, Blub!'")

    def clean_wings(self) -> None:
        pass

    def breath(self) -> None:
        self.__jump()
        print(f"and takes a deep breath")

    def __jump(self):
        print(f"{self._action_str_prefix()} jumping out of the water", end=" ")

    def spread_wings_underwater(self) -> None:
        print(f"{self._action_str_prefix()} spreading its wings underwater")

