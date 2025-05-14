from sirope import Sirope

class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    @staticmethod
    def find_by_email(srp, email):
        return srp.find_first(User, lambda u: u.email == email)

    @staticmethod
    def email_exists(srp, email):
        return User.find_by_email(srp, email) is not None

    def get_id(self):
        return self.email

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False