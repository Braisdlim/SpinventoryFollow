import os
from io import BytesIO
import requests
from config import Config
from .services.discogs_service import DiscogsService
from .models.disco import Disco

def save_disco(title: str, artist: str, cover_file=None) -> Disco:
    disco = Disco(title=title, artist=artist)
    
    # Opción 1: Subida manual de imagen
    if cover_file:
        cover_path = f"covers/{title}-{artist}.jpg"
        with open(os.path.join(Config.MEDIA_FOLDER, cover_path), "wb") as f:
            f.write(cover_file.read())
        disco.cover_path = cover_path
    
    # Opción 2: Buscar en Discogs si no hay imagen
    elif not disco.cover_path:
        cover_url = DiscogsService.get_cover(title, artist)
        if cover_url:
            # Descargar y guardar localmente
            response = requests.get(cover_url)
            cover_path = f"covers/{title}-{artist}-discogs.jpg"
            with open(os.path.join(Config.MEDIA_FOLDER, cover_path), "wb") as f:
                f.write(response.content)
            disco.cover_path = cover_path
    
    return disco