from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Chatroom(models.Model):
    chatroom_id = models.AutoField(
        db_column='chatroom_id',
        primary_key=True)

    name = models.CharField(max_length=20, blank=False)
    subject = models.CharField(max_length=145, blank=False)

    def __str__(self):
        return self.name



class Comment(models.Model):
    comment_id = models.AutoField(
        db_column= 'comment_id',
        primary_key=True)

    chatroom = models.ForeignKey(
        Chatroom, related_name='comment',
        on_delete=models.CASCADE)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
