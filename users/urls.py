from django.urls import path

from users.views import ProfileEditView

urlpatterns = [
    path('update/', ProfileEditView.as_view(), name='profile_edit'),
]
