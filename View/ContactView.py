from os import system
from Controllers.ContactController import ContactController
from Model.DTO.ContactForDelete import ContactForDelete
from Model.DTO.ContactForUpdate import ContactForUpdate
from Model.DTO.UserForView import UserForView


class ContactView:

    def __init__(self, user):
        self.user_logged = user

    def menu(self):
        while True:
            system("cls")
            print(" Menu de contactos ".center(50, "#"))
            print("1 - Lista de contactos")
            print("2 - Agregar contacto")
            print("3 - Editar contacto")
            print("4 - Eliminar contacto")
            print("5 - Cerrar sesion de usuario")
            print("-" * 50)
            option = input("Ingrese una opcion: ")
            if option == "1":
                self.list_contacts()
            elif option == "2":
                self.add_contact()
            elif option == "3":
                self.edit_contact()
            elif option == "4":
                self.delete_contact()
            elif option == "5":
                break
            else:
                print(" Opcion incorrecta ".center(50, "!"))
                input(" Presione enter para continuar ".center(50, "!"))

    def list_contacts(self):
        system("cls")
        print(" Lista de contactos ".center(50, "#"))
        contact_controller = ContactController()
        contacts = contact_controller.get_contacts_by_user(self.user_logged.username)
        for contact in contacts:
            print(contact)
        print("#" * 50)
        input(" Presione enter para continuar ".center(50, "!"))

    def add_contact(self):
        system("cls")
        print(" Alta de contacto ".center(50, "!"))
        print("-" * 50)
        name = input("Ingrese el nombre del contacto: ")
        print("-" * 50)
        surname = input("Ingrese el apellido del contacto: ")
        print("-" * 50)
        email = input("Ingrese el email del contacto: ")
        print("-" * 50)
        contact_controller = ContactController()
        contact_controller.add_contact(
            ContactForUpdate(0, name, surname, email, self.user_logged.username)
        )
        input(" Presione enter para continuar ".center(50, "!"))

    def edit_contact(self):
        system("cls")
        print(" Editar contacto ".center(50, "#"))
        print("-" * 50)
        id = input("Ingrese el id del contacto a editar: ")
        print("-" * 50)
        name = input("Ingrese el nombre del contacto: ")
        print("-" * 50)
        surname = input("Ingrese el apellido del contacto: ")
        print("-" * 50)
        email = input("Ingrese el email del contacto: ")
        print("-" * 50)
        contact_controller = ContactController()
        contact_controller.update_contact(
            ContactForUpdate(id, name, surname, email, self.user_logged.username)
        )
        input(" Presione enter para continuar ".center(50, "!"))

    def delete_contact(self):
        system("cls")
        print(" Eliminar contacto ".center(50, "!"))
        print("-" * 50)
        id = input("Ingrese el id del contacto a eliminar: ")
        print("-" * 50)
        contact_controller = ContactController()
        contact_controller.delete_contact(
            ContactForDelete(id, self.user_logged.username)
        )
        input(" Presione enter para continuar ".center(50, "!"))
