
from Model.Repository.UserRepository import UserRepository
from Model.Repository.ContactRepository import ContactRepository
from Controllers.UserController import UserController
from Model.Repository.AdminRepository import AdminRepository
from Model.DTO.AdminForLogin import AdminForLogin

class AdminController(UserController):
    
    def delete_forever(self, user):
        user_repository = UserRepository()
        contact_repository = ContactRepository()
        user_repository.delete_user(user)
        contact_repository.delete_contacts(user)
        
    def login(self, admin):
        admin_repository = AdminRepository()
        admin_from_repo = admin_repository.get_admin(admin)
        if admin_from_repo == None:
            return False, None
        else:
            admin_validated = AdminForLogin(admin_from_repo.username, admin_from_repo.password, admin_from_repo.token)
            if admin_from_repo.password == admin.password and admin_from_repo.token == admin.token:
                return True, admin_validated
            else:
                return False, admin_validated   
        