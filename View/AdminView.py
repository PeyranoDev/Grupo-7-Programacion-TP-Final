import hashlib
from Model.Entities.User import Admin
from Model.Repository.AdminRepository import AdminRepository
from Model.Repository.UserRepository import UserRepository

class AdminView:
    
    def __init__(self):
        self.repo = AdminRepository()
        self.user_repo = UserRepository()
    
    def hash_token(self, token):
        return hashlib.sha256(token.encode()).hexdigest()

    def login(self):
        username = input("Enter username: ")
        token = input("Enter token: ")
        hashed_token = self.hash_token(token)
        admin = self.repo.get_admin(username, hashed_token)
        if admin:
            print(f"Welcome, {admin.username}")
            return (True, admin)
        else:
            print("Invalid username or token.")
            return (False, None)

    def menu(self, admin):
        while True:
            print("Admin Menu")
            print("1. Create Admin")
            print("2. List Admins")
            print("3. Update Admin")
            print("4. Delete Admin")
            print("5. Manage Users")  # New option to manage users
            print("6. Logout")
            choice = input("Enter choice: ")
            
            if choice == "1":
                self.create_admin()
            elif choice == "2":
                self.list_admins()
            elif choice == "3":
                self.update_admin()
            elif choice == "4":
                self.delete_admin()
            elif choice == "5":
                self.manage_users()  # New method to manage users
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def create_admin(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        token = input("Enter token: ")
        
        admin = Admin(username=username, password=password, email=email, name=name, surname=surname, token=token)
        self.repo.add_admin(admin)
        print(f"Admin {username} created successfully.")
    
    def list_admins(self):
        with open(self.repo.file_path, "r") as file:
            admins = file.readlines()
            for row in admins:
                print(row.strip())
    
    def update_admin(self):
        username = input("Enter username of admin to update: ")
        token = input("Enter token: ")
        admin = self.repo.get_admin(username, self.hash_token(token))
        if admin:
            admin.password = input("Enter new password: ")
            admin.email = input("Enter new email: ")
            admin.name = input("Enter new name: ")
            admin.surname = input("Enter new surname: ")
            admin.token = self.hash_token(input("Enter new token: "))
            self.repo.update_admin(admin)
            print(f"Admin {username} updated successfully.")
        else:
            print("Admin not found.")
    
    def delete_admin(self):
        username = input("Enter username of admin to delete: ")
        self.repo.delete_admin(username)
        print(f"Admin {username} deleted successfully.")
    
    def manage_users(self):
        while True:
            print("User Management Menu")
            print("1. Delete User")
            print("2. Update User")
            print("3. View User Credentials")
            print("4. Help Users")
            print("5. Back to Admin Menu")
            choice = input("Enter choice: ")
            
            if choice == "1":
                self.delete_user()
            elif choice == "2":
                self.update_user()
            elif choice == "3":
                self.view_user_credentials()
            elif choice == "4":
                self.help_users()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def delete_user(self):
        username = input("Enter username of user to delete: ")
        self.user_repo.delete_user(username)
        print(f"User {username} deleted successfully.")
    
    def update_user(self):
        username = input("Enter username of user to update: ")
        user = self.user_repo.get_user(username)
        if user:
            user.password = input("Enter new password: ")
            user.email = input("Enter new email: ")
            user.name = input("Enter new name: ")
            user.surname = input("Enter new surname: ")
            self.user_repo.update_user(user)
            print(f"User {username} updated successfully.")
        else:
            print("User not found.")
    
    def view_user_credentials(self):
        username = input("Enter username of user to view: ")
        user = self.user_repo.get_user(username)
        if user:
            print(f"Username: {user.username}")
            print(f"Password: {user.password}")
            print(f"Email: {user.email}")
            print(f"Name: {user.name}")
            print(f"Surname: {user.surname}")
            print(f"State: {user.state}")
        else:
            print("User not found.")
    
    def help_users(self):
        print("Help section for users:")
        print("1. How to login")
        print("2. How to register")
        print("3. How to reset password")
        print("4. Back to User Management Menu")
        choice = input("Enter choice: ")
        
        if choice == "1":
            print("To login, enter your username and password on the login screen.")
        elif choice == "2":
            print("To register, go to the registration screen and fill in the required details.")
        elif choice == "3":
            print("To reset your password, click on 'Forgot password' and follow the instructions.")
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")
