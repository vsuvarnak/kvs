import random
import string


def generate_password(length: int = 10):
    alphabet = string.ascii_letters + string.digits
    passwd = ''.join(random.choice(alphabet) for i in range(length))
    return passwd


password = generate_password()
print(f"generated password: {password}")
