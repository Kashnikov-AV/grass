from django.core.management.utils import get_random_secret_key
SECRET_KEY = get_random_secret_key()

with open('grass/.env', 'w') as f:
    f.write(f'SECRET_KEY="{SECRET_KEY}"')
