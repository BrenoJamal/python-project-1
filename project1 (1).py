#!/usr/bin/env python3
"""
The oldest animal

@author: Breno Jamal
@date: 9/11/2024
"""


def oldest_animal(family):

    oldest_age = -1
    oldest_animals = []

    with open("zoo.txt", "r") as f:
        next(f) 
        for line in f:
            id, name, age, species, location = line.strip().split("\t")
            age = int(age)

            if family in species:
                if age > oldest_age:
                    oldest_age = age
                    oldest_animals = [name]
                elif age == oldest_age:
                    oldest_animals.append(name)

    if oldest_animals:
        oldest_animals.sort()
        return oldest_animals if len(oldest_animals) > 1 else oldest_animals[0]
    else:
        return None


def main():
    """Main function"""
    for a_species, expected in [
        ("Newt", "Wind"),
        ("Armadillo", "Cunning Fury"),
        ("Penguin", ["Underrated Thunder", "Wild Isotope"]),
        ("Jaguar", ["Chunk", "Thunder"]),
        ("Tiger", None),
        ("Zebra", None),
    ]:
        try:
            result = oldest_animal(a_species)
            assert (
                result == expected
            ), f"The oldest {a_species} in the zoo is {expected}, but {result} was returned instead"
            if result:
                print(f"The oldest {a_species} in the zoo is {result}.")
            else:
                print(f"Not a single {a_species} found.")
        except AssertionError as a_err:
            print(a_err)


if __name__ == "__main__":
    main()
