import json
import html

# ------------------ Hilfsfunktionen ------------------

def load_data(path):
    """Load JSON data from file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_name(animal):        return animal.get("name")
def get_diet(animal):        return animal.get("characteristics", {}).get("diet")
def get_type(animal):        return animal.get("characteristics", {}).get("type")
def get_locations(animal):
    locs = animal.get("locations", [])
    return ", ".join(locs) if locs else None

# ------------------ HTML-Serialisierung ------------------

def serialize_animal(animal):
    """Serialize a single animal into HTML list item (matching template)."""
    parts = ['<li class="cards__item">']

    name = get_name(animal)
    diet = get_diet(animal)
    locations = get_locations(animal)
    typ = get_type(animal)

    # Titel
    if name:
        parts.append(f'    <div class="card__title">{html.escape(name)}</div>')

    # Eigenschaften als Liste
    parts.append('    <div class="card__text">')
    parts.append('        <ul>')
    if diet:
        parts.append(f'            <li><strong>Diet:</strong> {html.escape(diet)}</li>')
    if locations:
        parts.append(f'            <li><strong>Location:</strong> {html.escape(locations)}</li>')
    if typ:
        parts.append(f'            <li><strong>Type:</strong> {html.escape(typ)}</li>')
    parts.append('        </ul>')
    parts.append('    </div>')

    parts.append('</li>')
    return "\n".join(parts)

def render_animals(data):
    """Return concatenated HTML of all animals."""
    return "\n".join(serialize_animal(a) for a in data)

# ------------------ Template-Ersetzung ------------------

def replace_placeholder(template_file, placeholder, replacement):
    """Replace placeholder in template with generated HTML."""
    with open(template_file, "r", encoding="utf-8") as f:
        content = f.read()
    if placeholder not in content:
        raise ValueError(f"Placeholder '{placeholder}' not found in template.")
    return content.replace(placeholder, replacement, 1)

# ------------------ Main ------------------

def main():
    data_file = "animals_data.json"
    template_file = "animals_template.html"
    output_file = "animals.html"
    placeholder = "{{ANIMALS}}"

    # JSON laden
    animals = load_data(data_file)
    if not animals:
        print("Keine Tiere in der JSON-Datei gefunden.")
        return

    # HTML für Tiere generieren
    animals_html = render_animals(animals)

    # Platzhalter im Template ersetzen
    final_html = replace_placeholder(template_file, placeholder, animals_html)

    # Ergebnis speichern
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"✔ {output_file} erfolgreich erzeugt!")

# ------------------ Skriptstart ------------------

if __name__ == "__main__":
    main()