import hashlib

class User:
    def __init__(self, username="", password="", email="", name="", surname="", state=True) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.surname = surname
        self.state = state

    def __repr__(self) -> str:
        return f"User(username={self.username}, password={self.password}, email={self.email}, name={self.name}, surname={self.surname}, state={self.state})"

class Admin(User):
    
    def __init__(self, username="", password="", email="", name="", surname="", state=True, token="") -> None:
        super().__init__(username, password, email, name, surname, state)
        self.token = self.hash_token(token)
        self.admin = True

    def hash_token(self, token):
        return hashlib.sha256(token.encode()).hexdigest()
        
    def __repr__(self) -> str:
        return f"Admin(username={self.username}, password={self.password}, email={self.email}, name={self.name}, surname={self.surname}, state={self.state})"
