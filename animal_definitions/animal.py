from animal_definitions.animal_behaviour import AnimalBehaviour
from abc import ABC, abstractmethod
from animal_definitions.gender import Gender
from datetime import date
from animal_definitions.diet import Diet


class Animal(AnimalBehaviour, ABC):

    def __init__(self, name: str, gender: Gender, species: str, diet: Diet, birthday: date, is_alive: bool):
        self.__name = name
        self.__gender = gender
        self.__species = species
        self.__diet = diet
        self.__birthday = birthday
        self.__is_alive = True

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: Gender):
        assert isinstance(gender, Gender), f"Gender must be of type Gender.MALE || Gender.FEMALE"
        self.__gender = gender

    @property
    def species(self):
        return self.__species

    @property
    def diet(self):
        return self.__diet

    @property
    def birthday(self) -> str:
        return f"{self.__birthday.day}.{self.__birthday.month}.{self.__birthday.year}"

    def has_birthday(self) -> None:
        self.__birthday += 1

    def get_age(self):
        days = (self.__birthday - date.today())
        return days // 365

    @property
    def is_alive(self) -> None:
        return self.is_alive

    @is_alive.setter
    def is_alive(self, is_alive: bool) -> None:
        assert isinstance(is_alive, bool), "Is alive value must be a boolean"
        self.is_alive = is_alive

    def sleep(self) -> None:
        print(f"{self.name} ({self.__name.__class__}) is sleeping")

    def eat(self) -> None:
        print(f"{self.__action_str_prefix()} eating {self.diet.value}")

    def __action_str_prefix(self) -> str:
        return f"{self.name} ({self.species}) is "

    @abstractmethod
    def move(self) -> None:
        pass

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def defend(self) -> None:
        pass

    @abstractmethod
    def make_sound(self) -> None:
        pass

    def __repr__(self):
        return f"Animal({self.name}, {self.gender}, {self.species}, {self.birthday}, {self.is_alive})"
