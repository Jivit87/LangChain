from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {"name":"Jivit", "age": "18"} 

print(new_person)