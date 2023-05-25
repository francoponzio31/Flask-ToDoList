from flask_login import UserMixin

class UserAuthModel(UserMixin):
    """
        User model for Flask Login 
    """
    def __init__(self, username, password):
        self.id = username
        self.password = password