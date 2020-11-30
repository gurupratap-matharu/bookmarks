from django.urls import path

from images.views import ImageCreateView, ImageDetailView

app_name = 'images'

urlpatterns = [
    path('create/', ImageCreateView.as_view(), name='create'),
    path('<slug:slug>/', ImageDetailView.as_view(), name='image_detail'),
]
