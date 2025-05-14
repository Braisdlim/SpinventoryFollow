from config import Config
from dataclasses import dataclass
import os

@dataclass
class Disco:
    title: str
    artist: str
    cover_path: str = None  # Ruta local (ej: "covers/portada.jpg")
    cover_url: str = None   # URL de la API (ej: "https://example.com/cover.jpg")

    @property
    def cover(self) -> str:
        if self.cover_path and os.path.exists(os.path.join(Config.MEDIA_FOLDER, self.cover_path)):
            return os.path.join(Config.MEDIA_FOLDER, self.cover_path)
        return self.cover_url or "static/images/default-cover.png"