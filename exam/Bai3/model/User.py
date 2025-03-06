class User:
    def __init__(self, id, email, username, password):
        self.id = id
        self.email = email
        self.username = username
        self.password = password
    def __str__(self):
        info = f"{self.id} - {self.email} - {self.username}"
        return info 
