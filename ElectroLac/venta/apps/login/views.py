from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView


# Create your views here.



class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account')
        return super.dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context


class LoginFormView2(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('account')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

