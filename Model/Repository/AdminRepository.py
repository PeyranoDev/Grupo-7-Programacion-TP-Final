from Model.Entities.User import Admin

class AdminRepository:
    
    def __init__(self):
        self.file_path = "Model/admins.txt"
        try:
            file = open(self.file_path, "r")
        except FileNotFoundError:
            print("Info Archivo: No se encontro el archivo de usuarios, se creara uno nuevo")
            file = open(self.file_path, "x")
        finally:
            file.close()
    
    def get_admin(self, admin, Token):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for row in lines:
                admin_data = row.strip().split(",")
                if (len(admin_data) == 7 and 
                    admin_data[0] == admin.username 
                    and admin_data[6] == Token 
                    and int(admin_data[6]) == 1):
                    
                    admin = Admin()
                    admin.username = admin_data[0]
                    admin.password = admin_data[1]
                    admin.email = admin_data[2]
                    admin.name = admin_data[3]
                    admin.surname = admin_data[4]
                    admin.token = int(admin_data[5])
                    admin.state = int(admin_data[6])
                    return admin
        return None