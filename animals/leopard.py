from datetime import date

from animal_definitions.diet import Diet
from animal_definitions.gender import Gender
from animal_types.terrestrial_animal import TerrestrialAnimal


class Leopard(TerrestrialAnimal):

    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, is_alive: bool, legs: int,
                 has_tail: bool):
        super().__init__(name, gender, species, diet, birthday, is_alive, 4)
        self.__has_tail = True

    def run(self):
        print(f"{self._action_str_prefix()} running at its top speed of 60kph")

    def play(self) -> None:
        print(f"{self._action_str_prefix()} playing hunting")

    def defend(self) -> None:
        print(f"{self._action_str_prefix()} defending its territory")

    def make_sound(self) -> None:
        print(f"{self.name}: 'Roar!'")
