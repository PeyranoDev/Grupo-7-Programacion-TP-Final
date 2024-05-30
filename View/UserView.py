from os import system
from Controllers.UserController import UserController
from Model.DTO.UserForDelete import UserForDelete
from Model.DTO.UserForCreation import UserForCreation
from Model.DTO.UserForLogin import UserForLogin


class UserView:

    def add_user_menu(self):
        system("cls")
        print(" Alta de usuario ".center(50, "#"))
        print("-" * 50)
        username = input("Ingrese el nombre de usuario: ")
        print("-" * 50)
        password = input("Ingrese la contraseña: ")
        print("-" * 50)
        email = input("Ingrese el email: ")
        print("-" * 50)
        name = input("Ingrese el nombre: ")
        print("-" * 50)
        surname = input("Ingrese el apellido: ")
        print("-" * 50)
        user_for_creation = UserForCreation(username, password, email, name, surname)
        user_controller = UserController()
        user_controller.add_user(user_for_creation)
        input(" Presione enter para continuar ".center(50, "!"))

    def login_menu(self):
        system("cls")
        print(" Login de usuario ".center(50, "#"))
        print("-" * 50)
        username = input("Ingrese el nombre de usuario: ")
        print("-" * 50)
        password = input("Ingrese la contraseña: ")
        print("-" * 50)
        input(" Presione enter para continuar ".center(50, "!"))
        user_controller = UserController()
        user_for_login = UserForLogin(username, password)
        validation = user_controller.login(user_for_login)
        return validation

    def list_users(self):
        system("cls")
        print(" Listado de usuarios ".center(50, "#"))
        user_controller = UserController()
        users = user_controller.get_users()
        for user in users:
            print(user)
        print("#" * 50)
        input(" Presione enter para continuar ".center(50, "!"))
        
    def delete_user_menu(self):
        system("cls")
        validation = self.login_menu()
        if validation[0]:
            selection = input("¿Está seguro que desea eliminar su usuario? (s/n): ")
            if selection.lower() != "s":
                input(" Presione enter para continuar ".center(50, "!"))
                return
            else:
                user = UserForDelete(validation[1].username)
                user_controller = UserController()
                user_controller.delete_user(user)
            input(" Presione enter para continuar ".center(50, "!"))
        else:
            print(" Usuario o contraseña incorrecta ".center(50, "!"))
            input(" Presione enter para continuar ".center(50, "!"))
            