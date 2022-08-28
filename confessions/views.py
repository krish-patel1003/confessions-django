from operator import truediv
from urllib import request
from django.shortcuts import render, HttpResponse
from .models import Confession

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
# CRUD
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)
# Create your views here.

dummy_confessions = [
    {
        "username": "user1",
        "confession": "This is a confession by user1"
    },
    {
        "username": "user2",
        "confession": "This is a confession by user2"
    },
    {
        "username": "user3",
        "confession": "This is a confession by user3"
    },
    {
        "username": "user4",
        "confession": "This is a confession by user4"
    },
    {
        "username": "user5",
        "confession": "This is a confession by user5"
    },
        {
        "username": "user1",
        "confession": "This is a confession by user1"
    },
    {
        "username": "user2",
        "confession": "This is a confession by user2"
    },
    {
        "username": "user3",
        "confession": "This is a confession by user3"
    },
    {
        "username": "user4",
        "confession": "This is a confession by user4"
    },
    {
        "username": "user5",
        "confession": "This is a confession by user5"
    },
]

def home(request):
    return render(request,
     template_name='confessions/confessions_home.html',
     context={"confessions":dummy_confessions})

class ConfListView(ListView):
    model = Confession
    template_name = 'confessions/confessions_home.html'
    ordering = ['-date_posted']
    context_object_name = 'confessions'
    paginate_by = 5

class ConfCreateView(LoginRequiredMixin, CreateView):
    model = Confession
    template_name = 'confessions/confession_create.html'
    fields = ["confession"]

    def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form)

class ConfDetailView(LoginRequiredMixin, DetailView):
    model = Confession

class ConfUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Confession
    template_name = 'confessions/confession_create.html'
    fields = ['confession']

    def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form)

    def test_func(self):
        conf = self.get_object()
        if self.request.user == conf.author:
            return True 
        return False

class ConfDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Confession
    template_name = 'confessions/confession_delete.html'
    success_url = '/'

    def test_func(self):
        conf = self.get_object()
        if self.request.user == conf.author:
            return True 
        return False 