from django.urls import path
from about.views import AboutMe

urlpatterns = [
    path('about-me/', AboutMe.as_view(), name = 'about')
]