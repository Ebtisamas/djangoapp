import os

# Set environment variables

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelProject.settings')

import django
# import basic settings for faker to work
django.setup()

import random
from model_app.models import Students
from faker import Faker

fakegen = Faker()

def populate(N):
    for e in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        student = Students.objects.get_or_create(
            first_name = fake_first_name,
            last_name = fake_last_name,
            email = fake_email
        )[0]


if __name__ == '__main__':
    print("Populating the DB")
    populate(20)
    print("Populating Complate")