from faker import Faker

from entities.base_entity import BaseEntity


class User(BaseEntity):

    def __init__(self, first_name: str, last_name: str, age: int, has_children_under_sixteen: bool, gender: str,
                 job: str, address: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.has_children_under_sixteen = has_children_under_sixteen
        self.gender = gender
        self.job = job
        self.address = address
        self.email = email

    @staticmethod
    def generateRandom():
        fake = Faker()
        gender = fake.random_element(elements=('F', 'M'))
        first_name = fake.first_name_female() if gender == 'F' else fake.first_name_male()
        last_name = fake.last_name_female() if gender == 'F' else fake.last_name_male()
        age = fake.pyint(10, 90)
        return User(
            first_name=first_name,
            last_name=last_name,
            age=age,
            has_children_under_sixteen=fake.pybool() if age in range(19, 60) else False,
            gender=gender,
            job=fake.job(),
            address=fake.address(),
            email=fake.email()
        )
