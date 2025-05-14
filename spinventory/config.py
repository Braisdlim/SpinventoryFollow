import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu-clave-secreta-aqui'
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    DISCOGS_TOKEN = os.environ.get('DISCOGS_TOKEN') or 'tu-token-de-discogs-aqui'  # Nueva línea
    MEDIA_FOLDER = os.path.join(os.path.dirname(__file__), "media")
    os.makedirs(MEDIA_FOLDER, exist_ok=True)  # Crea la carpeta si no existe