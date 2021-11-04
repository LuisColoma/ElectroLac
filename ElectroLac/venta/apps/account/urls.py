from . import views
from django.urls import path

from apps.account.views import *


urlpatterns = [
    #path("", LogoutView.as_view(), name='logout'),
    path("", views.create, name="create"),
    #path("",  UserCreateView.as_view(), name="create"),
]