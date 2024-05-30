class Contact:
    def __init__(self, id=0, name="", surname="", email="", username="", state=True) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.username = username
        self.state = state

    def __repr__(self) -> str:
        return f"Contact(id={self.id}, name={self.name}, surname={self.surname}, email={self.email}, username={self.username}, state={self.state})"
