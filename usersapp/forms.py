from django import forms
from django.contrib.auth.forms import UserCreationForm
from usersapp.models import CustomUser

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_pic']
