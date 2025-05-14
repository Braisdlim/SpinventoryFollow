import requests
from flask import current_app

class DiscogsService:
    @staticmethod
    def search_cover(artist, title):
        try:
            response = requests.get(
                "https://api.discogs.com/database/search",
                params={
                    "q": f"{artist} {title}",
                    "type": "release",
                    "key": current_app.config['DISCOGS_KEY'],
                    "secret": current_app.config['DISCOGS_SECRET']
                },
                headers={"User-Agent": "Spinventory/1.0"}
            )
            response.raise_for_status()
            data = response.json()
            return data["results"][0]["cover_image"] if data.get("results") else None
        except Exception as e:
            current_app.logger.error(f"Error en Discogs: {str(e)}")
            return None