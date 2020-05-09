import re
from data import users


class Registration:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @staticmethod
    def check_fields_length(field):
        return True if len(field) >= 8 else False

    def check_email_validation(self):
        return re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$",
                        self.email) is not None

    def check_password_validation(self):
        has_number = any(i.isdigit() for i in self.password)
        has_lower = self.password != self.password.upper()
        has_upper = self.password != self.password.lower()
        return has_number and has_lower and has_upper and self.check_fields_length(self.password)

    def check_password_confirmation(self):
        pass

    def registration(self):
        if self.check_email_validation() and self.check_password_validation():
            users.append({'email': self.email, 'password': self.password})
        else:
            return 'Invalid email or password format'


reg = Registration('ankitrai326sd@gmail.com', 'Prasdasdd3')
reg.registration()
print(users)

