import os

from exam.Bai3.IO.JSONFileFactory import JSONFileFactory
from exam.Bai3.model.User import User


class UserDAL:
    def __init__(self):
        self.list_user = []
        self.file_factory = JSONFileFactory()
    def add(self, new_user):
        self.list_user.append(new_user)
    def get_filepath(self, path):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, path)
        return str(filepath)
    def get_all_user(self):
        filepath = self.get_filepath("../data/user.json")
        self.list_user = self.file_factory.read_file(filepath, "r")
        list_user = []
        for user in self.list_user:
            temp_user = User(id=user["id"], email=user["email"], username=user["username"], password=user["password"])
            list_user.append(temp_user)
        return list_user
    def register_user(self, new_user):
        filepath = self.get_filepath("../data/user.json")
        self.file_factory.write_file(filepath, "w", new_user)
    def get_len(self):
        return len(self.list_user)
