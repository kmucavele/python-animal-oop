from abc import ABC, abstractmethod

from enclosures.enclosure_list import EnclosureIndex
from enclosures.enclosure_size import Size


class Enclosure(ABC):
    __total_enclosures = 0

    def __init__(self, name: str, capacity: int, size: Size, animal_species):
        self.__name = name
        self.__capacity = capacity
        self.__size = size
        self.__animal_species = animal_species
        self.__animals = EnclosureIndex(animal_species)  # enclosure list
        self.__total_animals = len(self.__animals.animal_list)
        self.__add_enclosure()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def capacity(self) -> int:
        return self.__capacity

    @property
    def size(self) -> Size:
        return self.__size.value

    @property
    def animals(self):
        return self.__animals

    @property
    def total_animals(self):
        return self.__total_animals

    @property
    def total_enclosures(self):
        return self.__total_enclosures

    @property
    def animal_species(self) -> str:
        return self.__animal_species.__name__

    def __add_enclosure(self):
        self.__total_enclosures += 1

    def add_animal(self, animal):
        if len(self.__animals.animal_list) < self.capacity:
            self.__animals.add_animal(animal)
            return
        print(f"Enclosure is full. Max capacity of {self.__capacity} was reached")

    def remove_animal(self, animal):
        self.__animals.remove_animal(animal)

    def feed(self):
        print("Animals are being fed")

    def empty_enclosure(self):
        self.__animals.remove_all_animals()
        print(f"{self.__animal_species.__name__} enclosure was emptied")

    @abstractmethod
    def clean(self):
        pass

    def __repr__(self) -> str:
        return f"Enclosure({self.name}, {self.capacity}, {self.size}, {self.animal_species}, {self.animals} )"
