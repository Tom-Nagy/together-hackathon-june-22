from django.urls import path
from . import views


urlpatterns = [
    path('', views.chatrooms, name='chatrooms'),
    path('chatroom/<int:chatroom_id>/', views.chatroom_detail, name='chatroom_detail'),

]
