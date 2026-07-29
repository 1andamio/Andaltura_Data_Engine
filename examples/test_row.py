from primer.models.row import Row


row = Row(
    name="Granada",
    population=230000,
)

print(row.name)

print(row["population"])

print(row.get("name"))

print(row.to_dict())

print("population" in row)

print(len(row))

print(row)