from django.db.models import Count
from django.http import HttpResponse
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from .form import *
from planets.models import *

menu = [
        {'title': 'Home', 'url_name': 'home'},
        {'title': 'Category', 'url_name': 'category'},
        {'title': 'About', 'url_name': 'about'},
    ]

class Home(ListView):
    model = Planets
    template_name = 'planets/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Home'
        return context

class Category_list(ListView):
    model = Planets
    template_name = 'planets/category.html'
    context_object_name = 'posts'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        context['cats'] = cats
        context['title'] = 'Category '
        context['menu'] = menu
        return context



class Cosmos(ListView):
    model = Planets
    template_name = 'planets/cosmos.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Planets.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        context['selected'] = self.kwargs['cat_slug']
        context['title'] = 'Category ' + self.kwargs['cat_slug']
        context['menu'] = menu
        return context

class RegisterUser(CreateView): #Регистрация
    form_class = RegisterUserForm
    template_name = 'planets/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        context['menu'] = menu
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class LoginUser(LoginView): #Авторизация
    form_class = LoginUserForm
    template_name = 'planets/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['menu'] = menu
        return context

    def get_success_url(self):
        return reverse_lazy('home')

class About(ListView):
    model = Planets
    template_name = 'planets/about.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        context['menu'] = menu
        return context

class Show_post(ListView):
    model = Planets
    template_name = 'planets/show_post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'cos_slug'


    def get_queryset(self):
        return Planets.objects.filter(slug=self.kwargs['cos_slug'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['cos_slug']
        context['menu'] = menu
        return context

class UserInfo(ListView):
    model = Planets
    template_name = 'planets/user.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User'
        context['menu'] = menu
        return context

def logout_user(request):   #Выход из учетной записи
    logout(request)
    return redirect('login')

class AddPage(CreateView):  #Добавление поля
    form_class = AddPostForm
    template_name = 'planets/add_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add'
        context['menu'] = menu
        return context

    def form_valid(self, form):
        form.save()

