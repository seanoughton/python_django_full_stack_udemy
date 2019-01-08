import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sean_first_project.settings')
import django
django.setup()

import random
from sean_first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    #[0] is there because Faker returns a tuple, and the first element in the tuple is a reference to the object instance
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()
        #create the fake data for that entry
        fake_url = fakegen.url() #creates a fake url
        fake_date = fakegen.date() #creates a fake date
        fake_name = fakegen.company() #creates a fake company name

        #create the new webage entry
        #for the ForeignKey info, you pass in the object this belongs to, not the id
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating scripts")
    populate(20)
    print("populating complete")
