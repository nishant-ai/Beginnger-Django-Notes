from django.urls import path
from .views import *

urlpatterns = [
    path('', create_view, name="create-view"),
    path('update-view/', update_view, name="update-view"),
    path('delete-view/', delete_view, name="delete-view"),
    path('users/', show_users, name="users")
]
