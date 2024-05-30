from os import system

from .ContactView import ContactView
from .UserView import UserView
from .AdminView import AdminView


class MainMenu:
    # Esta clase se encarga de manejar el menu que ve el usuario antes de loguearse. 
    def menu(self):
        while True:
            system("cls")
            print(" Bienvenido a la agenda de contactos ".center(50, "#"))
            print("1. Login de usuario")
            print("2. Registro de usuario")
            print("3. Listar Usuarios")
            print("4. Dar de baja usuario") # No implementado
            print("5. Login de administrador") # No implementado
            print("6. Salir del programa") 
            print("-" * 50)
            option = input("Ingrese una opcion: ")
            if option == "1":
                user_view = UserView()
                validation = user_view.login_menu()
                if validation[0] == True:
                    user = validation[1]
                    ContactView(user).menu()
                else:
                    print(" Usuario o contraseña incorrecta ".center(50, "!"))
                    input(" Presione enter para continuar ".center(50, "!"))
            elif option == "2":
                user_view = UserView()
                validation = user_view.add_user_menu()
            elif option == "3":
                user_view = UserView()
                validation = user_view.list_users()
            elif option == "4":
                user_view = UserView()
                validation = user_view.delete_user_menu()
            elif option == "5":
                admin_view = AdminView()
                validation = admin_view.login()
                if validation[0] == True:
                    admin = validation[1], validation[2]
                    admin_view.menu(admin)
            elif option == "6":
                print(" Saliendo del programa ".center(50, "!"))
                break
            else:
                print(" Opcion incorrecta ".center(50, "!"))
                input(" Presione enter para continuar ".center(50, "!"))


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.menu()
