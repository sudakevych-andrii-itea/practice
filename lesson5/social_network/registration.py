import re
import datetime


class Registration:
    users = []

    def __init__(self):
        self._email = None
        self._password = None
        self._confirm_password = None

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
        for user in self.__class__.users:
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
                    self.__class__.users.append({'id': len(self.__class__.users) + 1,
                                                 'email': self.email,
                                                 'password': self.password,
                                                 'registration_date': datetime.datetime.now().strftime('%d-%m-%Y %H:%M'),
                                                 'online': False})
                else:
                    return 'Passwords mismatch'
            else:
                return 'Invalid email or password format'
        else:
            return 'Email is already registered'
