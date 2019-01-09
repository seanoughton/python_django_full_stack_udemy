from django.db import models

class User(models.Model):

    first_name = models.CharField(max_length=264,unique=True)
    last_name = models.CharField(max_length=264,unique=True)
    email = models.EmailField(max_length=64,unique=True)

    def __str__(self):
        return self.last_name
