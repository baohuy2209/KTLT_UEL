class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def __str__(self):
        info = f"{self.username} - {self.password}"
        return info 