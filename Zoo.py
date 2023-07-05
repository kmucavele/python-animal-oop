from datetime import date

from animal_definitions.diet import Diet
from animal_definitions.gender import Gender
from animals.bat import Bat
from animals.flying_fish import FlyingFish
from animals.leopard import Leopard
from animals.octopus import Octopus
from enclosures.aquarium import Aquarium
from enclosures.enclosure_size import Size

if __name__ == '__main__':
    octopus_lisa = Octopus("Lisa", Gender.FEMALE, "Octopus", Diet.CARNIVORE, date(2020, 9, 29))
    octopus_carl = Octopus("Carl", Gender.MALE, "Octopus", Diet.CARNIVORE, date(2020, 9, 29))
    octopus_lonny = Octopus("Lonny", Gender.MALE, "Octopus", Diet.CARNIVORE, date(2020, 9, 29))

    flying_fish_walter = FlyingFish("Walter", Gender.MALE, "Flying Fish", Diet.HERBIVORE, date(2019, 2, 27))

    bat_betty = Bat("Betty", Gender.FEMALE, "Bat", Diet.CARNIVORE, date(2009, 7, 2), True)
    leopard_leo = Leopard("Leo", Gender.MALE, "Leopard", Diet.CARNIVORE, date(2015, 4, 13))

    octopus_aquarium = Aquarium("Octopus Aquarium", 2, Size.BIG, Octopus)

    print("Adding: Lisa to the Octopus aquarium: ")
    octopus_aquarium.add_animal(octopus_lisa)
    print(octopus_aquarium)

    print("Trying to add: Leo to the Octopus aquarium: ")
    octopus_aquarium.add_animal(leopard_leo)
    print(octopus_aquarium)

    print("Adding: Lonny to the Octopus aquarium: ")
    octopus_aquarium.add_animal(octopus_lonny)
    print(octopus_aquarium)

    print(f"""
    Print All Animals:
    {octopus_lisa}
    {flying_fish_walter}
    {bat_betty}
    {leopard_leo}
    """, end="\n")

    # ENCAPSULATION, INHERITANCE
    print(f"Species of Lisa: {octopus_lisa.species}")
    # returns an AttributeError: can't set attribute
    octopus_lisa.species = "Bat"

    print(f"Walters gender: {flying_fish_walter.gender}")
    # returns an assertions error
    flying_fish_walter.gender = "Female"

    flying_fish_walter.gender = Gender.FEMALE
    print(f"Walters new gender: {flying_fish_walter.gender}")

    # ABSTRACTION
    print(f"Get Waters age: {flying_fish_walter.get_age()}")

    print("Turn Betty into a vampire")
    bat_betty.turn_into_a_vampire()
    print(bat_betty)

    # POLYMORPHISM

    # Defend
    leopard_leo.defend()
    flying_fish_walter.defend()
    bat_betty.defend()
    octopus_lisa.defend()

    # Fly
    flying_fish_walter.fly()
    bat_betty.fly()
