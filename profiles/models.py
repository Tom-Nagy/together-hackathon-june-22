''' Models configuration for profiles app '''

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from chatrooms.models import Chatroom, Comment


class FavoritesChatrooms(models.Model):
    ''' Model that define the favorites chatroom database design '''

    class Meta:
        '''Set verbose name'''
        verbose_name_plural = 'Favorites Chatrooms'

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites_chatrooms')
    chatroom = models.ForeignKey(Chatroom, on_delete=models.SET_NULL,
                                 null=True, blank=True,)


class FavoritesComments(models.Model):
    ''' Model that define the favorites comment database design '''

    class Meta:
        '''Set verbose name'''
        verbose_name_plural = 'Favorites Comments'

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites_comments')
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL,
                                null=True, blank=True,)


class UserProfile(models.Model):
    ''' Model that define user profile information '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user_profile')
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
    instance.user_profile.save()
