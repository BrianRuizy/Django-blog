from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    # going to be using django created forms
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})