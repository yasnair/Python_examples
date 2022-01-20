from models import User
from database import session

user = User(
    username="admin"
)

session.add(user)  # Add the user
session.commit()  # Commit the change