import shelve

from registration import Registration


class Authentication(Registration):
    def __init__(self, email, password):
        super().__init__(email, password)

    @staticmethod
    def _login_to_account(user):
        with shelve.open('users') as users:
            users_dict = {
                'user_id': users[user]['user_id'],
                'email': users[user]['email'],
                'password': users[user]['password'],
                'registration_date': users[user]['registration_date'],
                'online': True
            }
            users[user] = users_dict

    @staticmethod
    def leave_account(user):
        with shelve.open('users') as users:
            users_dict = {
                'user_id': users[user]['user_id'],
                'email': users[user]['email'],
                'password': users[user]['password'],
                'registration_date': users[user]['registration_date'],
                'online': False
            }
            users[user] = users_dict

    def _check_email_existence(self):
        with shelve.open('users') as users:
            for user in users:
                if self._email == users.get(user)['email']:
                    return user
        return False

    def _check_password_match(self):
        user = self._check_email_existence()
        with shelve.open('users') as users:
            if self._password == users.get(user)['password']:
                return user

    @classmethod
    def get_users_list(cls):
        with shelve.open('users') as users:
            return [user for user in users.values()]

    def authentication(self):
        if self._check_email_existence():
            if self._check_password_match():
                user = self._check_password_match()
                self._login_to_account(user)
                return user
            else:
                return 'Invalid password'
        else:
            return 'This email address does not exist'
