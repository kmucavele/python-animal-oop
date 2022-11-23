from datetime import date

from animal_definitions.diet import Diet
from animal_definitions.gender import Gender
from animal_types.flying_animal import FlyingAnimals


class Bat(FlyingAnimals):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, is_alive: bool,
                 lays_eggs: bool):
        super().__init__(name, gender, species, diet, birthday, is_alive, False)

    def play(self) -> None:
        print(f"{self._action_str_prefix()} practicing hunting")

    def sleep(self) -> None:
        print(f"{self.sleep()} upsidedown")

    def defend(self) -> None:
        print(f"{self._action_str_prefix()} is not defending itself, because all predators are asleep at night")

    def make_sound(self) -> None:
        print(f"{self.name}: 'Squeak!'")

    def clean_wings(self) -> None:
        print(f"{self._action_str_prefix()} cleaning its wings")

    def turn_into_a_vampire(self) -> None:
        self.__species = "🧛🏻"
        print(f"Bat ({self.name}) turned into a vampire: {self.species}")

    def give_birth(self) -> None:
        print(f"{self._action_str_prefix()} giving birth")
