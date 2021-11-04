from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from apps.erp.mixins import ValidatePermissionRequiredMixin
#from apps.account.forms import UserForm

# Create your views here.


def create(request):
    return render(request, 'account/registrar.html')
