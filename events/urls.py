''' url configuration for chatroom app '''

from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_events, name='all_events'),

]
