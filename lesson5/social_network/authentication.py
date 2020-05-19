from registration import Registration


class Authentication(Registration):
    def __init__(self):
        super().__init__()

    @staticmethod
    def _login_to_account(user):
        user['online'] = True

    @staticmethod
    def leave_account(user):
        user['online'] = True

    def _check_email_existence(self):
        for user in self.__class__.users:
            if self._email == user['email']:
                return user
        return False

    def _check_password_match(self):
        user = self._check_email_existence()
        if self._password == user['password']:
            return user

    @classmethod
    def get_users_list(cls):
        return cls.users

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
