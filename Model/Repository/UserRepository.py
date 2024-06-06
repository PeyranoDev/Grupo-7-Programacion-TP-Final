from Model.Entities.User import User

class UserRepository:
    
    def __init__(self):
        self.file_path = "Model/users.txt"
        try:
            file = open(self.file_path, "r")
        except FileNotFoundError:
            print("Info Archivo: No se encontró el archivo de usuarios, se creará uno nuevo")
            file = open(self.file_path, "x")
        finally:
            file.close()
    
    def get_user(self, username):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for row in lines:
                user_data = row.strip().split(",")
                if user_data[0] == username:
                    user = User(
                        username=user_data[0],
                        password=user_data[1],
                        email=user_data[2],
                        name=user_data[3],
                        surname=user_data[4],
                        state=bool(int(user_data[5]))
                    )
                    return user
        return None
    
    def add_user(self, user):
        with open(self.file_path, "a") as file:
            file.write(f"{user.username},{user.password},{user.email},{user.name},{user.surname},{int(user.state)}\n")
    
    def update_user(self, user):
        users = []
        with open(self.file_path, "r") as file:
            users = file.readlines()
        
        with open(self.file_path, "w") as file:
            for row in users:
                user_data = row.strip().split(",")
                if user_data[0] == user.username:
                    file.write(f"{user.username},{user.password},{user.email},{user.name},{user.surname},{int(user.state)}\n")
                else:
                    file.write(row)
    
    def delete_user(self, username):
        users = []
        with open(self.file_path, "r") as file:
            users = file.readlines()
        
        with open(self.file_path, "w") as file:
            for row in users:
                user_data = row.strip().split(",")
                if user_data[0] != username:
                    file.write(row)
