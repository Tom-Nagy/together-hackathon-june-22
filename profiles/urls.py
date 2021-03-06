''' url configuration for profile app '''

from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('edit_make_profile_public_status/',
         views.edit_make_profile_public_status,
         name='edit_make_profile_public_status'),
]
