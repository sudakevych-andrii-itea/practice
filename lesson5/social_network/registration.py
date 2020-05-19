import re
import datetime
import shelve


class Registration:

    def __init__(self, email, password, confirm_password=None):
        self._email = email
        self._password = password
        self._confirm_password = confirm_password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def confirm_password(self):
        return self._confirm_password

    @confirm_password.setter
    def confirm_password(self, value):
        self._confirm_password = value

    @staticmethod
    def _check_fields_length(field):
        return True if len(field) >= 8 else False

    def _check_email_validation(self):
        return re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$",
                        self._email) is not None

    def _check_email_originality(self):
        with shelve.open('users') as users:
            if len(users):
                for user in users.values():
                    if user['email'] == self._email:
                        return False
        return True

    def _check_password_validation(self):
        has_number = any(i.isdigit() for i in self._password)
        has_lower = self._password != self._password.upper()
        has_upper = self._password != self._password.lower()
        return has_number and has_lower and has_upper and self._check_fields_length(self._password)

    def _check_password_confirmation(self):
        return self._password == self._confirm_password

    def registration(self):
        if self._check_email_originality():
            if self._check_email_validation() and self._check_password_validation():
                if self._check_password_confirmation():
                    users_dict = {
                        'email': self.email,
                        'password': self.password,
                        'registration_date': datetime.datetime.now().strftime('%d-%m-%Y %H:%M'),
                        'online': False
                    }
                    with shelve.open('users') as users:
                        users_dict.update(user_id=f'{len(users) + 1}')
                        users[f'{len(users) + 1}'] = users_dict

                else:
                    return 'Passwords mismatch'
            else:
                return 'Invalid email or password format'
        else:
            return 'Email is already registered'
