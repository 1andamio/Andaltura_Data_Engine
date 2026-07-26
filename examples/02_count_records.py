from primer.services.wfs import WFSClient

client = WFSClient(
    "https://www.ideandalucia.es/wfs-nga-inspire/services"
)

print("Consultando número total de entidades...")

response = client.request(
    request="GetFeature",
    typeNames="gn:NamedPlace",
    resultType="hits",
)

print()
print(response.text)

client.close()