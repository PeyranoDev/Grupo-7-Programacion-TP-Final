from Model.DTO.ContactForView import ContactForView
from Model.Repository.ContactRepository import ContactRepository


class ContactController:

    def get_contacts_by_user(self, username):
        contact_repository = ContactRepository()
        contacts = contact_repository.get_contacts_by_user(username)
        contacts_for_view = []
        for contact in contacts:
            contact_for_view = ContactForView(contact)
            contacts_for_view.append(contact_for_view)
        return contacts_for_view

    def get_contact(self, contact):
        contact_repository = ContactRepository()
        contact = contact_repository.get_contact(contact)
        contact_for_view = ContactForView(contact)
        return contact_for_view

    def add_contact(self, contact):
        contact_repository = ContactRepository()
        contact_repository.add_contact(contact)

    def update_contact(self, contact):
        contact_repository = ContactRepository()
        contact_repository.update_contact(contact)

    def delete_contact(self, contact):
        contact_repository = ContactRepository()
        contact_repository.delete_contact(contact)
