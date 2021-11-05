from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
#from apps.login.views import *
#from apps.account.views import *

urlpatterns = [
    path("", LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='login.html'), name='logout'),

]