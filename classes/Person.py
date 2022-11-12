class Person:

    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.birthday = data['birthday']
        self.country = data['country']
        self.country_code = data['country_code']
        self.city = data['city']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}, {self.city}, {self.country}'