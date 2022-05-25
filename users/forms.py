from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile  

# Creamos una instancia de UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #Adding fields

    #Class Meta gives us a neested namespace for configurations and keeps the configs in one place and within the configs with are saying that the model will be efective 
    # is the user model so for the form.save is going to save it to this user model and the fields that we have here in this list are the fields that we want in the form and in that order.
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']