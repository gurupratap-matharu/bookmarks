import logging
from urllib import request

from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from images.models import Image

logger = logging.getLogger(__name__)


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("title", "url", "description")
        widgets = {
            "url": forms.HiddenInput,
            "description": forms.Textarea(attrs={"cols": 80, "rows": 5}),
        }

    def clean_url(self):
        url = self.cleaned_data["url"]
        valid_extensions = ["jpg", "jpeg"]
        extension = url.rsplit(".", 1)[1].lower()
        logger.info("clean_url: extension: %s", extension)

        if extension not in valid_extensions:
            raise forms.ValidationError(
                "The given url does not match valid image extensions."
            )
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        obj = super().save(commit=False)
        image_url = self.cleaned_data["url"]
        extension = image_url.rsplit(".", 1)[1].lower()
        name = slugify(obj.title)
        image_name = f"{name}.{extension}"
        logger.info("ImageCreateForm: save(): image_name: %s...", image_name)

        # download the image from the given url
        response = request.urlopen(image_url)

        obj.image.save(image_name, ContentFile(response.read()), save=False)

        logger.info("ImageCreateForm: image downloaded successfully...")

        if commit:
            obj.save()
            logger.info("ImageCreateForm: obj saved...")

        return obj
