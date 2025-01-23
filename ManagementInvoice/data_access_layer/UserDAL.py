from ManagementInvoice.io.JSONFileFactory import JSONFileFactory
from ManagementInvoice.models.User import User


class UserDAL:
    def __init__(self):
        self.list_user = []
    def get_all_users(self):
        json_factory = JSONFileFactory()
        self.list_user = json_factory.read_file("data/user.json", "r")
        list_user = []
        for user in self.list_user:
            element_user = User(username = user["username"], password = user["password"])
            list_user.append(element_user)
        return list_user