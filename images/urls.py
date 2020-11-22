from django.urls import path

from images.views import ImageCreateView

app_name = 'images'

url_patterns = [
    path('create/', ImageCreateView.as_view(), name='create'),
]
