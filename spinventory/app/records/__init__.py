from flask import Blueprint
from .routes import records_bp
from ..services.discogs_service import DiscogsService  # Añade esta línea

# ... resto del código ...