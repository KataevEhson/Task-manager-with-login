from django.urls import path, include
from .views import *

urlpatterns = [
    path("", registration, name="registration"),
    path("profile/", profile, name="profile"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),   
    path("create_task/", create_task, name="create_task"),
    path("show_task/", show_task, name="my_task"),
    path('update_task/<int:pk>', update_task, name='update_task'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),
]
