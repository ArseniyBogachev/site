from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm): #Добавление поля
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Сategory not selected'

    class Meta:
        model = Planets
        fields = ['title', 'slug', 'content', 'is_published', 'photo', 'cat']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__post_input'}),
            'slug': forms.TextInput(attrs={'class': 'form__post_input'}),
            'content': forms.Textarea(attrs={'class': 'form__post_input-content'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form__post_input-boolean'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form__post_input-photo'}),
            'cat': forms.Select(attrs={'class': 'form__post_input'}),
        }



class RegisterUserForm(UserCreationForm):   #Регистрация
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form__post_input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form__post_input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form__post_input'}))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form__post_input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):    #Авторизация
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form__post_input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form__post_input'}))