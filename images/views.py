import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.views.generic.detail import DetailView

from images.forms import ImageCreateForm
from images.models import Image

logger = logging.getLogger(__name__)


class ImageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Image
    form_class = ImageCreateForm
    template_name = "images/image_form.html"
    success_message = "%(title)s successfully created"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "GET":
            kwargs.update(
                {
                    "data": self.request.GET,
                }
            )
        return kwargs

    def form_valid(self, form):
        logger.info("form_valid: assigning user...")
        form.instance.user = self.request.user
        return super().form_valid(form)


class ImageDetailView(LoginRequiredMixin, DetailView):
    model = Image
    template_name = "images/image_detail.html"
    context_object_name = "image"
