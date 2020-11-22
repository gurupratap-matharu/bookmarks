import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from images.forms import ImageCreateForm

logger = logging.getLogger(__name__)


class ImageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ImageCreateForm
    template_name = 'images/image_form.html'
    success_message = "%(title) successfully created"

    def form_valid(self, form):
        logger.info('form_valid: assigning user...')
        form.instance.user = self.request.user
        return super().form_valid(form)
