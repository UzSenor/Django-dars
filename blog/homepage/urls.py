from .views import homePageView
from homepage.urls import path

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
]