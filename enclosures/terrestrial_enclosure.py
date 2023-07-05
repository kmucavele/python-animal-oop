from enclosures.enclosure import Enclosure
from enclosures.enclosure_size import Size


class TerrestrialEnclosure(Enclosure):

    def __init__(self, name: str, capacity: int, size: Size, animal_species, terrain: str):
        super().__init__(name, capacity, size, animal_species)
        self.__terrain = terrain

    def clean(self):
        print(f"The {self.animal_species} enclosure is being temporary emptied and cleaned")

    @property
    def terrain(self):
        return self.__terrain
