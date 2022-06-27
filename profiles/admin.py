from django.contrib import admin
from .models import UserProfile, FavoritesChatrooms, FavoritesComments


class AdminFavoritesChatrooms(admin.ModelAdmin):
    list_display = (
        'user',
        'chatroom',
    )
    ordering = ('user', 'chatroom',)


class AdminFavoritesComments(admin.ModelAdmin):
    list_display = (
        'user',
        'comment',
    )
    ordering = ('user', 'comment',)


class AdminUserProfile(admin.ModelAdmin):
    list_display = (
        'user',
        'about',
        'image',
        'make_public',
    )
    ordering = ('user',)


admin.site.register(FavoritesChatrooms, AdminFavoritesChatrooms)
admin.site.register(FavoritesComments, AdminFavoritesComments)
admin.site.register(UserProfile, AdminUserProfile)
