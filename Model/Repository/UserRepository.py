from ..Entities.User import User

class UserRepository:

    def __init__(self):
        self.file_path = "Model/users.txt"
        try:
            file = open(self.file_path, "r")
        except FileNotFoundError:
            print("Info Archivo: No se encontro el archivo de usuarios, se creara uno nuevo")
            file = open(self.file_path, "x")
        finally:
            file.close()

    def get_users(self):
        users = []
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for row in lines:
                user_data = row.strip().split(",")
                if len(user_data) == 6 and int(user_data[5]) == 1:
                    user = User()
                    user.username = user_data[0]
                    user.password = user_data[1]
                    user.email = user_data[2]
                    user.name = user_data[3]
                    user.surname = user_data[4]
                    user.state = int(user_data[5])
                    users.append(user)
        return users

    def get_user(self, user):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for row in lines:
                user_data = row.strip().split(",")
                if (len(user_data) == 6 and user_data[0] == user.username and int(user_data[5]) == 1):
                    user = User()
                    user.username = user_data[0]
                    user.password = user_data[1]
                    user.email = user_data[2]
                    user.name = user_data[3]
                    user.surname = user_data[4]
                    user.state = int(user_data[5])
                    return user
        return None

    def add_user(self, user):
        with open(self.file_path, "a") as file:
            file.write(f"{user.username},{user.password},{user.email},{user.name},{user.surname},1\n")
            
    def deactivate_user(self, username):
        lines = []
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        with open(self.file_path, "w") as file:
            for row in lines:
                user_data = row.strip().split(",")
                if len(user_data) == 6 and user_data[0] == username:
                    user_data[5] = '0'
                file.write(",".join(user_data) + "\n")
                
    def delete_user_forever(self, username):
        lines = []
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        with open(self.file_path, "w") as file:
            for row in lines:
                user_data = row.strip().split(",")
                if len(user_data) == 6 and user_data[0] != username:
                    file.write(",".join(user_data) + "\n")

