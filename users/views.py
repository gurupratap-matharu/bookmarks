from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from users.forms import ProfileEditForm


class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = ProfileEditForm
    success_url = reverse_lazy('home')
    template_name = 'profile_edit.html'
