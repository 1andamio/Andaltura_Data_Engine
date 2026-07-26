from primer.services.wfs import WFSClient

client = WFSClient(
    "https://www.ideandalucia.es/wfs-nga-inspire/services"
)

print(client.get_capabilities()[:1000])

client.close()