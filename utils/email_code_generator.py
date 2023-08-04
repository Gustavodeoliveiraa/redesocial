import secrets
import string


def code_generator():
    num = string.digits
    code = ''.join(secrets.choice(num) for _ in range(6))
    return code


if __name__ == '__main__':
    print(code_generator())