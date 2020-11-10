from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from users.forms import ProfileUpdateForm
from users.models import Profile


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'users/profile_.html'
