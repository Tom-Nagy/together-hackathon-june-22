''' Models configuration for profiles app '''

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    ''' Model that define user profile information '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user_profile')
    username = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    make_public = models.BooleanField(default=False)

    def __str__(self):
        ''' Return the username '''
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    ''' Create or upadte the user profile '''
    if created:
        UserProfile.objects.create(user=instance)
    # If existing user, just save
    instance.userprofile.save()
