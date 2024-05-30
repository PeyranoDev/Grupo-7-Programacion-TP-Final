from os import system
from Controllers.AdminController import AdminController
from Model.DTO.AdminForLogin import AdminForLogin

class AdminView():

    def login(self):
        system("cls")
        print(" Login de administrador ".center(50, "#"))
        print("-" * 50)
        username = input("Ingrese el nombre de usuario: ")
        print("-" * 50)
        password = input("Ingrese la contraseña: ")
        print("-" * 50)
        token = input("Ingrese el token seguro: ")
        print("-" * 50)
        input(" Presione enter para continuar ".center(50, "!"))
        admin_controller = AdminController()
        admin_for_login = AdminForLogin(username, password, token)
        validation = admin_controller.login(admin_for_login)
        return validation
        
    def menu(self, admin):
        while True:
            system("cls")
            print(" Bienvenido administrador ".center(50, "#"))
            print("1. Listar usuarios (Con sus credenciales)")
            print("2. Eliminar permanentemente un usuario")
            print("3. Editar credenciales de un usuario")
            print("4. Editar información de un usuario")
            print("5. Salir del menu de administrador")
            print("-" * 50)
            option = input("Ingrese una opcion: ")
            if option == "1":
                admin_controller = AdminController()
                validation = self.login()
                if validation[0]:
                    users = admin_controller.get_users(admin)
                    for user in users:
                        print(user)
                    input(" Presione enter para continuar ".center(50, "!"))
            elif option == "2":
                admin_controller = AdminController()
                validation = self.login()
                if validation[0]:
                    username = input("Ingrese el nombre de usuario a eliminar: ")
                    admin_controller.delete_forever(username)
                    input(" Presione enter para continuar ".center(50, "!"))
                else:
                    print(" Usuario, contraseña o token incorrecto ".center(50, "!"))
                    input(" Presione enter para continuar ".center(50, "!"))
            elif option == "3":
                admin_controller = AdminController()
                validation = self.login()
                if validation[0]:
                    username = input("Ingrese el nombre de usuario a editar: ")
                    new_username = input("Ingrese el nuevo nombre de usuario: ")
                    new_password = input("Ingrese la nueva contraseña: ")
                    admin_controller.edit_credentials(username, new_username, new_password)
                    input(" Presione enter para continuar ".center(50, "!"))
                else:
                    print(" Usuario, contraseña o token incorrecto ".center(50, "!"))
                    input(" Presione enter para continuar ".center(50, "!"))
            elif option == "4":
                admin_controller = AdminController()
                validation = self.login()
                if validation[0]:
                    username = input("Ingrese el nombre de usuario a editar: ")
                    new_email = input("Ingrese el nuevo email: ")
                    new_name = input("Ingrese el nuevo nombre: ")
                    new_surname = input("Ingrese el nuevo apellido: ")
                    admin_controller.edit_info(username, new_email, new_name, new_surname)
                    input(" Presione enter para continuar ".center(50, "!"))
                else:
                    print(" Usuario, contraseña o token incorrecto ".center(50, "!"))
                    input(" Presione enter para continuar ".center(50, "!"))
            elif option == "5":
                print(" Saliendo del menu de administrador ".center(50, "!"))
                break
            else:
                print(" Opcion incorrecta ".center(50, "!"))
                input(" Presione enter para continuar ".center(50, "!"))
            
