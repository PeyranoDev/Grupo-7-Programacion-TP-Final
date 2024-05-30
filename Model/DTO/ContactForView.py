class ContactForView:
    def __init__(self, contact) -> None:
        self.name = contact.name
        self.surname = contact.surname
        self.email = contact.email
        self.username = contact.username
        self.id = contact.id

    def __str__(self) -> str:
        return f"Nombre: {self.name} - Apellido: {self.surname} - Email: {self.email} - Id: {self.id}"
