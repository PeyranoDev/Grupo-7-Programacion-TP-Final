class ContactForUpdate:
    def __init__(self, id=0, name="", surname="", email="", username="") -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.username = username
        self.state = 1
