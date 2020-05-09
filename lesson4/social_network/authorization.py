from registration import Registration


class Authorization(Registration):
    def __init__(self, email, password):
        super().__init__(email, password)


auth = Authorization('sdf', 'sdfsdf')
print(auth.example())
