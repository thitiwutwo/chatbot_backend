from django.urls import path
from .views  import *
urlpatterns = [
    path('', Home),
    path('login', Login),
    path('CheckRegister', CheckRegister),
    path('all-user/', all_users),
    path('post-user/', add_user),
    path('update-user/<int:UID>', update_user),
    path('delete-user/<int:UID>', delete_user),
]