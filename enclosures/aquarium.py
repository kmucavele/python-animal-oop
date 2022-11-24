from enclosures.enclosure import Enclosure
from enclosures.enclosure_list import EnclosureIndex
from enclosures.enclosure_size import Size


class Aquarium(Enclosure):

    def __init__(self, name: str, capacity: int, size: Size, animal_species):
        super().__init__(name, capacity, size, animal_species)
        self.__water_plants = set()

    def clean(self):
        print(f"The {self.animal_species} are put in smaller aquariums and the water is changed")

    @property
    def water_plants(self):
        return self.water_plants

    def add_water_plant(self, *water_plant):
        self.__water_plants.add(water_plant)

    def remove_water_plant(self, *water_plant):
        self.__water_plants.remove(water_plant)
