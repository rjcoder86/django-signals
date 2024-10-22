from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)

    # def create_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #         print('****************')
    #         print('Profile created!')
    #         print('****************')

    # post_save.connect(create_profile, sender=User)
    