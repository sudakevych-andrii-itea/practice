from registration import Registration
from authentication import Authentication
from user import User, Admin

reg1 = Registration()
reg1.email = 'email@gmail.com'
reg1.password = 'Password1'
reg1.confirm_password = 'Password1'
reg1.registration()
reg2 = Registration()
reg2.email = 'email1@gmail.com'
reg2.password = 'Password1'
reg2.confirm_password = 'Password1'
reg2.registration()
print(Registration.users)

auth1 = Authentication()
auth1.email = 'email1@gmail.com'
auth1.password = 'Password1'
auth1.authentication()

user1 = User()
user1.current_user = auth1.authentication()
user1.add_post('Lorem ipsum')
user1.add_post('Ipsum lorem')
print(user1.get_posts())

auth1.leave_account(user1.current_user)

auth2 = Authentication()
auth2.email = 'email@gmail.com'
auth2.password = 'Password1'
auth2.authentication()

user2 = Admin()
user2.current_user = auth2.authentication()
print(user2.get_users_posts_info(Authentication.get_users_list()))
