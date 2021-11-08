from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
#from django.core.urlresolvers import reverse_lazy
#from django.urls import reverse
from django.urls import reverse

class RegistrarUsuario(CreateView):
   model=User
   template_name="registration/registrar.html"
   form_class=UserCreationForm
   success_url= reverse_lazy('')

from django.shortcuts import render, redirect
from .forms import RegisterForm


from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
   if response.method == "POST":
      form = RegisterForm(response.POST)
      if form.is_valid():
         form.save()   
         return redirect("../events/index.html")
   else:
         form = RegisterForm()
   return render(response, "registration/registrar.html", {"form":form})

