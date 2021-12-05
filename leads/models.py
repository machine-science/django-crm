from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE

# user = get_user_model()

# Create your models here.


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    '''
    We need to link leads and agents models.
    This model will allow us to do the same
    These models need to get attached to specific userprofile.
    This userprofile is linked to user in the Agent model. Then each
    agent link back to it's parent userprofile.
    This is done to show / view relavant information to that particular logged in 
    lead/agent  
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


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

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    # here foreign key allows to have many Agents for one User
    # What we want is to have one Agent per One User
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Hence we will use one to one mapping

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # We do not need first and last name sice we are inheriting it
    # from AbstractUser

    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.user.email


def post_user_created_signal(sender, instance, created, **kwargs):
    """
    This function will be called when post_save event is received.
    The event that gets sent to this function, gives us bunch of parameters that we can work with.

    :param sender: is the actual sender
    :param instance: is the actual model that was saved (for eg. User)
    :param created: Which tells us whetehr or not the model was created

    """
    # print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
# The way we do that is by taking the signal, and signal has method called
# connect. The connect takes in the name of the function you want to call and
# need to specify sender, the sender is the exact model that is sending the event.
