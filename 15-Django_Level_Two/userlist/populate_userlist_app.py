import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','userlist.settings')
import django
django.setup()

import random
from userlist_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        #create the fake data for that entry
        fake_first_name = fakegen.first_name_male() #creates a fake name
        fake_last_name = fakegen.last_name_female() #creates a fake name
        fake_email = fakegen.email() #creates a fake name

        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]



if __name__ == '__main__':
    print("populating scripts")
    populate(20)
    print("populating complete")
