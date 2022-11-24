from datetime import date

from animal_definitions.diet import Diet
from animal_definitions.gender import Gender
from animal_types.flying_animal import FlyingAnimals


class Bat(FlyingAnimals):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, lays_eggs: bool,
                 ability=None):
        super().__init__(name, gender, species, diet, birthday, False)
        self.__ability = ability

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
        self.__ability = "🧛🏻"
        print(f"Bat ({self.name}) turned into a vampire: {self.species}")

    def give_birth(self) -> None:
        print(f"{self._action_str_prefix()} giving a life birth")

    def __repr__(self) -> str:
        return f"Animal({self.name}, {self.gender}, {self.species}, {self.birthday}, {self.is_alive}, {self.__ability})"
