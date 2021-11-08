from . import views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
#from apps.login.views import *
#from apps.account.views import *
from apps.registro.views import RegistrarUsuario
from apps.registro import views
from django.urls import path
from apps.registro import views
from . import views
urlpatterns = [
    #path("", views.registro, name='registro'),
 #  url(r'',RegistrarUsuario.as_view(),name="registro"),
   #path('registro/',views.apps.registro,name='registro'),
    path("", views.register, name="register"),  # <-- added
]