from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=30, required=False, help_text='What would I call you without a name?')
    last_name = forms.CharField(label='Last Name', max_length=30, required=False, help_text='We would like to direct you via last name!')
    email = forms.EmailField(label='Email', max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )