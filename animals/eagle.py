from datetime import date

from animal_definitions.diet import Diet
from animal_definitions.gender import Gender
from animal_types.flying_animal import FlyingAnimals


class Eagle(FlyingAnimals):
    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, is_alive: bool,
                 lays_eggs: bool):
        super().__init__(name, gender, species, diet, birthday, is_alive, True)

    def play(self) -> None:
        print(f"{self._action_str_prefix()} practicing hunting")

    def defend(self) -> None:
        print(f"{self._action_str_prefix()} defending its territory")

    def make_sound(self) -> None:
        print(f"{self.name}: 'Screech!'")

    def fly_15_000_feet_high(self) -> None:
        print(f"{self.fly()} 15.000 feet high (4.572 km)")

