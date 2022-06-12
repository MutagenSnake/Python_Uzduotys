sarasas = [2.5, 2, "Labas", True, False, 5, 7, 8, 2.8, "Vakaras", 1]

print(sum([element for element in sarasas if type(element) == int or type(element) == float]))
[print(element) for element in sarasas if type(element) is str]
[print(element) for element in sarasas if element is True]