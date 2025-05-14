from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
    
    def get_id(self):
        return self.email

class Record:
    def __init__(self, title, artist, year, genre, condition, user_email, cover_url=None):
        self.title = title
        self.artist = artist
        self.year = year
        self.genre = genre
        self.condition = condition
        self.user_email = user_email
        self.cover_url = cover_url or self._generate_default_cover()  # Asegura que siempre haya una URL

    def _generate_default_cover(self):
        """Genera una portada por defecto basada en los datos del disco"""
        base_color = hash(f"{self.artist}{self.title}") % 360
        return f"https://fakeimg.pl/400x400/{base_color},128/333333,255/?text={self.artist[0]}+{self.title[0]}&font_size=75"