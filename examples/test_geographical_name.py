from primer.models.common.geographical_name import GeographicalName

name = GeographicalName(
    text="EF A-6050",
    language="spa",
    nativeness="endonym",
    name_status="other",
    source="Nomenclátor Geográfico de Andalucía.",
    script="Latn",
)

print(name)
print(name.text)
print(name.language)
print(name.script)