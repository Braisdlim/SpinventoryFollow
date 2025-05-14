import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DiscogsService:
    @staticmethod
    def get_cover(artist, title):
        try:
            response = requests.get(
                "https://api.discogs.com/database/search",
                params={
                    "q": f"{artist} {title}",
                    "type": "release",
                    "key": os.getenv("DISCOGS_KEY"),
                    "secret": os.getenv("DISCOGS_SECRET")
                },
                headers={"User-Agent": "Spinventory/1.0"}
            )
            response.raise_for_status()
            data = response.json()
            return data["results"][0]["cover_image"] if data["results"] else None
        except Exception as e:
            print(f"Error fetching cover: {e}")
            return None