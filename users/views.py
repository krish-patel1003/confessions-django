from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'users/user_create.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    success_message = "Your profile was created successfully"

