from accounts.models import User


def make_user(name, password, email):
    User.objects.create(
        username=name, email=email, password=password
    )