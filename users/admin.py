from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.models import Profile

from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['user', 'date_of_birth', 'photo']


class ProfileInLine(admin.TabularInline):
    model = Profile


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInLine,)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
