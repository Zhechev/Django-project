from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.URLField()

    @receiver(post_save, sender=User) # Still don't know how, but next rows create ProfileUser when User is created
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ProfileUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profileuser.save()

    def __str__(self):
        return f"{self.user}"
