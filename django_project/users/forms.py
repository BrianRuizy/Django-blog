from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# create new form that inhereits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    # Gives us nested namespace for configuration
    class Meta: 
        model = User  # form.save() will save it to this user model
        fields = ['username', 'email', 'password1', 'password2']  # Form fields and order