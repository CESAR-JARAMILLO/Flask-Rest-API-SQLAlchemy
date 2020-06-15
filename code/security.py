from werkzeug.security import safe_str_cmp
from user import User


# Authenticate user
def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

# Payload is the content of the JWT token
def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
