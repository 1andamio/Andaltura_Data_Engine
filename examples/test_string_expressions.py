from dataclasses import dataclass

from primer.query.field import Field


@dataclass
class City:
    name: str


city = City("Sierra Nevada")

print(Field("name").contains("Nev"))
print(Field("name").startswith("Sierra"))
print(Field("name").endswith("Nevada"))

print(Field("name").contains("Nev")(city))
print(Field("name").startswith("Sierra")(city))
print(Field("name").endswith("Nevada")(city))
print(Field("name").contains("Granada")(city))