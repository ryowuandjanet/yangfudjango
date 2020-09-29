from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
  username = forms.CharField(max_length=20)
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-text with-border', 'placeholder': 'Password'}))
  fullname = forms.CharField(widget=forms.HiddenInput())
  class Meta(UserCreationForm.Meta):
    model = CustomUser
    fields = ('username','first_name','last_name', 'email','fullname' ) # new

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = ('username', 'email', ) # new