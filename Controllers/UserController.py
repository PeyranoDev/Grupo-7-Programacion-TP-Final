from Model.DTO.UserForLogin import UserForLogin
from Model.Repository.UserRepository import UserRepository
from Model.DTO.UserForView import UserForView
from Model.Repository.ContactRepository import ContactRepository

class UserController:

    def get_users(self):
        user_repository = UserRepository()
        users = user_repository.get_users()
        users_for_view = []
        for user in users:
            user_for_view = UserForView(user)
            users_for_view.append(user_for_view)
        return users_for_view

    def get_user(self, user):
        user_repository = UserRepository()
        user_from_repo = user_repository.get_user(user)
        if user_from_repo == None:
            return None
        else:
            user_for_view = UserForView(user_from_repo)
            return user_for_view

    def login(self, user):
        user_repository = UserRepository()
        user_from_repo = user_repository.get_user(user)
        if user_from_repo == None:
            return False, None
        else:
            user_validated = UserForLogin(user_from_repo.username, user_from_repo.password)
            if user_from_repo.password == user.password:
                return True, user_validated
            else:
                return False, user_validated     
                
    def add_user(self, user):
        user_repository = UserRepository()
        user_repository.add_user(user)
        
    def delete_user(self, user):
        user_repository = UserRepository()
        contact_repository = ContactRepository()
        user_repository.deactivate_user(user.username)
        contact_repository.deactivate_contacts(user.username)