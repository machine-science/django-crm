from django.db import models
from django.contrib.auth.models import AbstractUser

# user = get_user_model()

# Create your models here.


class User(AbstractUser):
    pass


class Lead(models.Model):

    # source_choices = (
    #     ('YouTube', 'YouTube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter'),
    # )

    # The Lead is not going to be associated with User, it is
    # more of a record of personal info

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    # # check if any lead is phoned or not
    # phoned = models.BooleanField(default=False)
    # # sourse of the lead
    # source = models.CharField(choices=source_choices, max_length=100)
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_file = models.FileField(blank=True, null=True)


class Agent(models.Model):
    # here foreign key allows to have many Agents for one User
    # What we want is to have one Agent per One User
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Hence we will use one to one mapping

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # We do not need first and last name sice we are inheriting it
    # from AbstractUser

    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
