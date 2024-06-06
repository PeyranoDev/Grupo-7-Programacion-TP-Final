from Model.Entities.User import Admin
import hashlib

class AdminRepository:
    
    def __init__(self):
        self.file_path = "Model/admins.txt"
        try:
            file = open(self.file_path, "r")
        except FileNotFoundError:
            print("Info Archivo: No se encontró el archivo de admins, se creará uno nuevo")
            file = open(self.file_path, "x")
        finally:
            file.close()
    
    def get_admin(self, username, token):
        hashed_token = self.hash_token(token)
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for row in lines:
                admin_data = row.strip().split(",")
                if (len(admin_data) == 7 and 
                    admin_data[0] == username and 
                    admin_data[5] == hashed_token and 
                    int(admin_data[6]) == 1):
                    
                    admin = Admin(
                        username=admin_data[0],
                        password=admin_data[1],
                        email=admin_data[2],
                        name=admin_data[3],
                        surname=admin_data[4],
                        token=admin_data[5],
                        state=bool(int(admin_data[6]))
                    )
                    return admin
        return None
    
    def add_admin(self, admin):
        with open(self.file_path, "a") as file:
            file.write(f"{admin.username},{admin.password},{admin.email},{admin.name},{admin.surname},{admin.token},1\n")
    
    def update_admin(self, admin):
        admins = []
        with open(self.file_path, "r") as file:
            admins = file.readlines()
        
        with open(self.file_path, "w") as file:
            for row in admins:
                admin_data = row.strip().split(",")
                if admin_data[0] == admin.username:
                    file.write(f"{admin.username},{admin.password},{admin.email},{admin.name},{admin.surname},{admin.token},1\n")
                else:
                    file.write(row)
    
    def delete_admin(self, username):
        admins = []
        with open(self.file_path, "r") as file:
            admins = file.readlines()
        
        with open(self.file_path, "w") as file:
            for row in admins:
                admin_data = row.strip().split(",")
                if admin_data[0] != username:
                    file.write(row)

    def hash_token(self, token):
        return hashlib.sha256(token.encode()).hexdigest()
