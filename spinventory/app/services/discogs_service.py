import requests
from config import Config

class DiscogsService:
    @staticmethod
    def get_cover(album: str, artist: str) -> str:
        try:
            response = requests.get(
                "https://api.discogs.com/database/search",
                params={
                    "release_title": album,
                    "artist": artist,
                    "token": Config.DISCOGS_TOKEN,
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            return data["results"][0]["cover_image"] if data.get("results") else None
        except (requests.RequestException, KeyError) as e:
            print(f"Error al llamar a Discogs: {e}")
            return None