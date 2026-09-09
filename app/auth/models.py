import hashlib
import os

class User:
    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email 
        self.salt = os.urandom(16)  # Generate a random salt
        self.password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.salt, 100_000)  # Hash the password with the salt
        self.role = role 

    def verify_password(self, password):
        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            self.salt,
            100_000
        )
        return password_hash == self.password_hash

class Admin(User):
    def __init__(self, name, email, password,):
        super().__init__(name, email, password, role='admin')



class Player(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, role='player')

