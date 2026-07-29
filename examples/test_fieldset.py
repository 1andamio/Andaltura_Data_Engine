from primer.query.fieldset import FieldSet


fields = FieldSet(
    "name",
    "population",
    "province.name",
)

print(fields)

print(len(fields))

print(fields.names())

print("population" in fields)

for field in fields:
    print(field.path)