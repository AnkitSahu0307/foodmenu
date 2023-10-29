from .models import Profile
from django.db.models.signals import post_save
# post save becz we want a signal when the user data is saved.
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save,sender=User)
#added receiver as decorator to this fun.and also name the sender.
def build_profile(sender,instance,created,**kwargs):
    #check if user is created 
    #if created means that we want to create the profile object.
    if created :
        Profile.objects.create(user=instance)
#So we actually want to fire up this function when the user profile is created.
#how we know that profile is created -- by using post_save signal
#and after recening the signal execute this function

# to save the profile need another function
@receiver(post_save,sender=User)
# this also need to receive the signal
def save_profile(sender,instance,**kwargs):
    instance.profile.save()