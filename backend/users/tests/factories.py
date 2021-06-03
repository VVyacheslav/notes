from factory import DjangoModelFactory, Faker

from users.models import User


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")

    def __new__(cls, *args, **kwargs) -> User:
        return super().__new__(*args, **kwargs)

    class Meta:
        model = User
        django_get_or_create = ["username"]
