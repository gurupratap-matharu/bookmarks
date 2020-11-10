from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from users.forms import ProfileUpdateForm
from users.models import Profile


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'


class ProfileUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ['bio', 'location', 'date_of_birth', 'photo']
    template_name = 'users/profile_update_form.html'
    success_message = 'Profile updated successfully!'
