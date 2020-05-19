from registration import Registration
from authentication import Authentication
from user import User, Admin
import shelve

reg1 = Registration('email@gmail.com', 'Password1', 'Password1')
reg1.registration()
reg2 = Registration('email1@gmail.com', 'Password1', 'Password1')
reg2.registration()

with shelve.open('users') as users:
    for user in users.items():
        print(user)

auth1 = Authentication('email@gmail.com', 'Password1')
auth1.authentication()

user1 = User(auth1.authentication())
user1.add_post('Lorem ipsum')
user1.add_post('Ipsum lorem')
print(user1.get_posts())

auth1.leave_account(user1.current_user)

auth2 = Authentication('email1@gmail.com', 'Password1')
auth2.authentication()

user2 = Admin(auth2.authentication())
print(user2.get_users_posts_info())
