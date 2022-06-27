from django.contrib import admin
from .models import Chatroom, Comment


# Register your models here.
class AdminChatroom(admin.ModelAdmin):
    list_display = (
        'name',
        'subject',
    )


class AdminComment(admin.ModelAdmin):
    list_display = (
        'chatroom',
        'user',
        'date',
    )


admin.site.register(Chatroom, AdminChatroom)
admin.site.register(Comment, AdminComment)
