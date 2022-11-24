from enclosures.enclosure import Enclosure
from enclosures.enclosure_list import EnclosureIndex
from enclosures.enclosure_size import Size


class Cage(Enclosure):

    def __init__(self, name: str, capacity: int, size: Size, animal_species):
        super().__init__(name, capacity, size, animal_species)
        self.__hanging_decoration = []

    def clean(self):
        print(f"The {self.animal_species} are put in smaller cages and the cage is being cleaned")

    @property
    def hanging_decoration(self):
        return self.__hanging_decoration

    def add_hanging_decoration(self, *hanging_decoration):
        self.__hanging_decoration.append(hanging_decoration)

    def remove_hanging_decoration(self, *hanging_decoration):
        self.__hanging_decoration.remove(hanging_decoration)
