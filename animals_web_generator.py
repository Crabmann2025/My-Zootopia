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


def get_animal_string(animal):
    """Returns the information of an animal as a string"""
    output = ''  # leere Zeichenkette definieren

    name = get_name(animal)
    diet = get_diet(animal)
    location = get_location(animal)
    typ = get_type(animal)

    if name:
        output += f"Name: {name}\n"
    if diet:
        output += f"Ernährung: {diet}\n"
    if location:
        output += f"Lebensraum: {location}\n"
    if typ:
        output += f"Typ: {typ}\n"

    output += "\n"  # Leerzeile zwischen den Tieren
    return output


def get_all_animals_string(data):
    """Iterates through all animals and returns a single string"""
    output = ''
    for animal in data:
        output += get_animal_string(animal)
    return output


if __name__ == "__main__":
    animals = load_data("animals_data.json")
    all_animals_text = get_all_animals_string(animals)
    print(all_animals_text)  # Optional: Ausgabe auf dem Bildschirm