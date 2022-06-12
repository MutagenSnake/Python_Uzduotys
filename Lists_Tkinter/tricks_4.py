from operator import attrgetter

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return f'Vardas: {self.vardas} ir amžius: {self.amzius}'

person1 = Zmogus("Petras", 50)
person2 = Zmogus("Jonas", 70)
person3 = Zmogus("Juozas", 35)

list_of_persons = [person1, person2, person3]

sorted_by_name = sorted(list_of_persons, key=attrgetter("vardas"), reverse=True)
sorted_by_age = sorted(list_of_persons, key=attrgetter("amzius"), reverse=True)
pass