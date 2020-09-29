from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  list_display = ["username","email","first_name","last_name","fullname"]
  model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
