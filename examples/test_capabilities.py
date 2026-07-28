from primer.services.wfs.client import WFSClient
from primer.services.wfs.capabilities import CapabilitiesAnalyzer

WFS_URL = "https://www.ideandalucia.es/wfs-nga-inspire/services"

client = WFSClient(WFS_URL)

cap = CapabilitiesAnalyzer(client).load()

print("\n=== CAPABILITIES ===")
print(f"Título............: {cap.service_title}")
print(f"Versión...........: {cap.version}")
print(f"Proveedor.........: {cap.provider}")
print(f"Paginación........: {cap.supports_paging}")
print(f"Ordenación........: {cap.supports_sorting}")
print(f"Count por defecto.: {cap.count_default}")

print("\nFeature Types:")
for ft in cap.feature_types:
    print(f" - {ft}")