people = [
    {"name": "Harry", "house": "Gryffindor"}
    {"name": "cho", "house": "Ravenclaw"}
    {"name": "Draco", "house": "Slytherin"}
]
def f(person):
    return person["name"]
    

people.sort()

print(people)
    

people.sort(key=lambda person: person["name"])

print(people) 


