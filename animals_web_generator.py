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

def serialize_animal(animal):
    """Serialize a single animal as HTML"""
    output = '<li class="cards__item">\n'

    name = get_name(animal)
    diet = get_diet(animal)
    location = get_location(animal)
    typ = get_type(animal)

    if name:
        output += f'<div class="card__title">{name}</div>\n'
    output += '<p class="card__text">\n'
    if diet:
        output += f'    <strong>Diet:</strong> {diet}<br/>\n'
    if location:
        output += f'    <strong>Location:</strong> {location}<br/>\n'
    if typ:
        output += f'    <strong>Type:</strong> {typ}<br/>\n'
    output += '</p>\n'
    output += '</li>\n'

    return output

def get_all_animals_html(data):
    """Iterates over all animals and returns a complete HTML string"""
    output = ''
    for animal in data:
        output += serialize_animal(animal)
    return output

if __name__ == "__main__":
    animals = load_data("animals_data.json")
    all_animals_html = get_all_animals_html(animals)
    print(all_animals_html)  # Optional: Output on the screen