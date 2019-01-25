from django.db import models
#this imports the User model that comes automatically with django admin
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    #this is a model class to add information that the default user does not have
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additonal attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)



    def __str__(self):
        return self.user.username
