class EnclosureIndex:

    def __init__(self, animal_species):
        """animal_species = an animal class e.g. Bat, Octopus, etc."""
        self.__animal_species = animal_species
        self.__animal_list = set()

    @property
    def animal_list(self) -> set:
        return self.__animal_list

    def add_animal(self, animal):
        assert issubclass(animal.__class__, self.__animal_species), \
            f"This enclosure only can hold animals of type: " \
            f"{self.__animal_species.__name__} "
        self.__animal_list.add(animal)

    def remove_animal(self, animal):
        if animal in self.__animal_list:
            self.__animal_list.remove(animal)
            return
        print(f"{animal} is not in this enclosure")

    def remove_all_animals(self):
        self.__animal_list.clear()

    def __repr__(self):
        return f"{self.animal_list}"
