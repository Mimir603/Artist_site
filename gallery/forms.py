from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваше сообщение', 'rows': 4})
    )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')