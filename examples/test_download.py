from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from primer.datasets.dataset import Dataset
from primer.acquisition.download_manager import DownloadManager

dataset = Dataset(
    id="test",
    name="Archivo de prueba",
    url="https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore",
)

with DownloadManager() as manager:
    result = manager.download(dataset)

print()
print("Éxito   :", result.success)
print("Mensaje :", result.message)
print("Archivo :", result.file)
print("Tamaño  :", result.size)
print("SHA256  :", result.checksum)