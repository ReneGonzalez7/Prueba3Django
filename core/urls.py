from signal import signal
from django.urls import path
from .views import home, create, update, delete, SignUpView#, updateUser, deleteUser;

urlpatterns = [
    path('', home, name="home"),
    path('createUser', SignUpView.as_view(), name="createUser"),
    #path('updateUser', updateUser, name="updateUser"),
    #path('deleteUser', deleteUser, name="deleteUser"),
    path('create', create, name="create"),
    path('update/<id>', update, name="update"),
    path('delete/<id>', delete, name="delete"),
]