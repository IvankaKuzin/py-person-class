class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = []

    for person_data in people:
        person = Person(name=person_data.get("name"),
                        age=person_data.get("age"))
        person_list.append(person)

    for person_data in people:
        person = Person.people[person_data.get("name")]
        if "wife" in person_data and person_data.get("wife"):
            person.wife = Person.people[person_data.get("wife")]
        if "husband" in person_data and person_data.get("husband"):
            person.husband = Person.people[person_data.get("husband")]

    return person_list
