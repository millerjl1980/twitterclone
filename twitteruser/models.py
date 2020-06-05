from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)
    #https://stackoverflow.com/questions/16613013/model-self-dependency-one-to-many-field-implementation/16614136#16614136
    followers = models.ManyToManyField('self',blank=True,null=True)

    def __str__(self):
        return self.display_name