from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
#from apps.login.views import *
#from apps.account.views import *

urlpatterns = [
    
    path("", views.registro, name='registro'),

]