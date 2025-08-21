import json


def load_data(dateipfad):
    """Load JSON-Data"""
    with open(dateipfad, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_name(animal):
    """Returns the name if available"""
    return animal.get("name")


def get_diet(animal):
    """Returns nutrition if present"""
    return animal.get("characteristics", {}).get("diet")


def get_location(animal):
    """Returns the first location, if any"""
    locations = animal.get("locations", [])
    return locations[0] if locations else None


def get_type(animal):
    """Returns the type if any"""
    return animal.get("characteristics", {}).get("type")


def print_animals(animal):
    """Displays the information of an animal"""
    name = get_name(animal)
    diet = get_diet(animal)
    location = get_location(animal)
    typ = get_type(animal)

    if name:
        print(f"Name: {name}")
    if diet:
        print(f"diet: {diet}")
    if location:
        print(f"location: {location}")
    if typ:
        print(f"Typ: {typ}")
    print()


def animal_print(data):
    """Iterates through all animals"""
    for animal in data:
        print_animals(animal)


if __name__ == "__main__":
    animals = load_data("animals_data.json")
    animal_print(animals)