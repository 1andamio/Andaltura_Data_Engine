"""
Manifest de descargas del importador SIMA.

Versión 2.0
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path


class Manifest:
    VERSION = "2.0"

    def __init__(self, manifest_file: str | Path, data_directory: str | Path, source: str = "SIMA") -> None:
        self.path = Path(manifest_file)
        self.data_directory = Path(data_directory)
        self.source = source

        if self.path.exists():
            self._load()
        else:
            self.data = {
                "version": self.VERSION,
                "source": self.source,
                "created_at": self._now(),
                "updated_at": self._now(),
                "summary": {},
                "municipalities": {},
            }
            self._update_summary()

    @staticmethod
    def _now() -> str:
        return datetime.now().isoformat(timespec="seconds")

    def _load(self) -> None:
        with self.path.open("r", encoding="utf-8") as f:
            self.data = json.load(f)

    def save(self) -> None:
        self.data["updated_at"] = self._now()
        self._update_summary()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def start(self, code: str, name: str, province: str) -> None:
        self.data["municipalities"].setdefault(code, {
            "name": name,
            "province": province,
            "status": "pending",
            "downloads": {
                "ficha": {"downloaded": False, "file": None, "size": 0, "sha256": None},
                "nucleos": {"downloaded": False, "file": None, "size": 0, "sha256": None},
            },
            "started_at": None,
            "finished_at": None,
            "elapsed_seconds": None,
            "error": None,
        })

    def begin(self, code: str) -> None:
        m = self.data["municipalities"][code]
        m["status"] = "running"
        m["started_at"] = self._now()

    def set_download(self, code: str, document: str, file: str, size: int) -> None:
        p = self.data_directory / file
        sha = None
        if p.exists():
            h = hashlib.sha256()
            with p.open("rb") as f:
                for chunk in iter(lambda: f.read(65536), b""):
                    h.update(chunk)
            sha = h.hexdigest()
        self.data["municipalities"][code]["downloads"][document] = {
            "downloaded": True,
            "file": file,
            "size": size,
            "sha256": sha,
        }

    def complete(self, code: str, elapsed_seconds: float) -> None:
        m = self.data["municipalities"][code]
        m["status"] = "completed"
        m["finished_at"] = self._now()
        m["elapsed_seconds"] = round(elapsed_seconds, 3)
        m["error"] = None

    def fail(self, code: str, message: str) -> None:
        m = self.data["municipalities"][code]
        m["status"] = "failed"
        m["finished_at"] = self._now()
        m["error"] = str(message)

    def status(self, code: str):
        return self.data["municipalities"].get(code, {}).get("status")

    def is_completed(self, code: str) -> bool:
        return self.status(code) == "completed"

    def rebuild(self) -> None:
        for folder in sorted(self.data_directory.iterdir()):
            if not folder.is_dir():
                continue
            code = folder.name
            ficha = folder / "ficha.html"
            nucleos = folder / "nucleos.html"
            if code not in self.data["municipalities"]:
                self.start(code, code, "")
            m = self.data["municipalities"][code]
            ok = True
            for doc, fp in (("ficha", ficha), ("nucleos", nucleos)):
                if fp.exists():
                    self.set_download(code, doc, str(fp.relative_to(self.data_directory)), fp.stat().st_size)
                else:
                    ok = False
            m["status"] = "completed" if ok else "pending"
        self.save()

    def _update_summary(self):
        c=f=r=p=0
        for m in self.data["municipalities"].values():
            s=m["status"]
            if s=="completed": c+=1
            elif s=="failed": f+=1
            elif s=="running": r+=1
            else: p+=1
        self.data["summary"]={"total":len(self.data["municipalities"]),"completed":c,"failed":f,"running":r,"pending":p}

    @property
    def summary(self):
        self._update_summary()
        return self.data["summary"]
