from .views import homePageView
from django.urls import path

urlpatterns = [
    path('', homePageView, name='home'),
]