# small contact book to practice dicts, lists and sets

contacts = {}


def add_contact(name, phone, tags):
    contacts[name] = {"phone": phone, "tags": set(tags)}


def find_by_tag(tag):
    result = []
    for name, info in contacts.items():
        if tag in info["tags"]:
            result.append(name)
    result.sort()
    return result


add_contact("Ana", "45 99999-1111", ["work", "college"])
add_contact("Bruno", "45 98888-2222", ["college"])
add_contact("Carla", "45 97777-3333", ["work", "work"])

print("all contacts:", ", ".join(sorted(contacts)))
print("college:", find_by_tag("college"))
print("work:", find_by_tag("work"))
print("Carla tags:", contacts["Carla"]["tags"])

# tuple unpacking
name, phone = "Ana", contacts["Ana"]["phone"]
print(name, "->", phone)
