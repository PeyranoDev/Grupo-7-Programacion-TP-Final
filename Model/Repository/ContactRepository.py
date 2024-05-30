import os
from ..Entities.Contact import Contact


class ContactRepository:

    def __init__(self):
        self.file_path = "Model/contacts.txt"
        try:
            file = open(self.file_path, "r")
        except FileNotFoundError:
            print("Info Archivo: No se encontro el archivo de contactos, se creara uno nuevo")
            file = open(self.file_path, "x")
        finally:
            file.close()

    def get_contacts_by_user(self, username):
        contacts = []
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                contact_data = line.strip().split(",")
                if len(contact_data) == 6 and contact_data[4] == username and int(contact_data[5]) == 1:
                    contact = Contact()
                    contact.id = int(contact_data[0])
                    contact.name = contact_data[1]
                    contact.surname = contact_data[2]
                    contact.email = contact_data[3]
                    contact.username = contact_data[4]
                    contact.state = int(contact_data[5])
                    contacts.append(contact)
        return contacts

    def get_contact(self, contact):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                contact_data = line.strip().split(",")
                if len(contact_data) == 6 and contact_data[0] == contact.id:
                    contact.name = contact_data[1]
                    contact.surname = contact_data[2]
                    contact.email = contact_data[3]
                    contact.username = contact_data[4]
                    contact.state = int(contact_data[5])
                    break
        return contact

    def add_contact(self, contact):
        with open(self.file_path, "a") as file:
            contact.id = self._get_next_id()
            line = f"{contact.id},{contact.name},{contact.surname},{contact.email},{contact.username},{contact.state}\n"
            file.write(line)
        return contact

    def update_contact(self, contact, new_state=1):
        lines = []
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        with open(self.file_path, "w") as file:
            for line in lines:
                contact_data = line.strip().split(",")
                if (len(contact_data) == 6 and contact_data[0] == contact.id and contact_data[4] == contact.username):
                    if new_state == 0:
                        line = f"{contact.id},{contact_data[1]},{contact_data[2]},{contact_data[3]},{contact_data[4]},{new_state}\n"
                    else:
                        line = f"{contact.id},{contact.name},{contact.surname},{contact.email},{contact.username},{new_state}\n"
                file.write(line)

    def delete_contact(self, contact):
        self.update_contact(contact, 0)

    def deactivate_contacts(self, username):
        lines = []
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        with open(self.file_path, "w") as file:
            for line in lines:
                contact_data = line.strip().split(",")
                if len(contact_data) == 6 and contact_data[4] == username:
                    contact_data[5] = '0'
                file.write(",".join(contact_data) + "\n")

    def _get_next_id(self):
        if not os.path.exists(self.file_path):
            return 1
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                last_contact_data = last_line.strip().split(",")
                if len(last_contact_data) == 6:
                    return int(last_contact_data[0]) + 1
        return 1
