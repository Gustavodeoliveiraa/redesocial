import re
from django.core.exceptions import ValidationError


def add_class_field(field, attr_name, attr_new_val):
    exist = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{exist} {attr_new_val}'.strip()


def strong_password(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not pattern.match(password):
        raise ValidationError((
                'Password must contain at least 1 lowercase letter'
                '1 uppercase letter, 1 number and 8 or more characters'
            ),
                code='invalid',
            )


if __name__ == '__main__':
    nome = "Gustavoakves30423"

    print(strong_password(nome))