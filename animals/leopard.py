from datetime import date

from animal_definitions.diet import Diet
from animal_definitions.gender import Gender
from animal_types.terrestrial_animal import TerrestrialAnimal


class Leopard(TerrestrialAnimal):

    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date):
        super().__init__(name, gender, species, diet, birthday, 4, True)

    def run(self):
        print(f"{self._action_str_prefix()} running at its top speed of 60kph")

    def play(self) -> None:
        print(f"{self._action_str_prefix()} playing hunting")

    def defend(self) -> None:
        print(f"{self._action_str_prefix()} defending its territory")

    def make_sound(self) -> None:
        print(f"{self.name}: 'Roar!'")
