from django.urls import path
from .views  import *
urlpatterns = [
    path('', Home),
    path('login', Login),
    # CRUD user table
    path('all-user/', all_users),
    path('post-user/', add_user),
    path('update-user/<int:UID>', update_user),
    path('delete-user/<int:UID>', delete_user),

    # CRUD file table
    path('upload-file', upload_file),
    path('get-file/', get_all_files),
    path('get-file/<slug:INTENT>', get_file),

    # CRUD chat table
    path('get-chat/', get_chat),
    path('get-chat/<int:CID>', get_chat_by_channel),
    path('create-chat', create_chat),

    # CRUD channel table
    path('get-channel/', get_channel),
    path('get-channel/<int:CID>', get_channel_by_id),
    path('get-channel/user/<int:UID>', get_channel_by_user),
    path('create-channel', create_channel),
    path('delete-channel/<int:CID>', delete_channel),

]