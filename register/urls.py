from django.urls import path
from . import views



urlpatterns = [
    path('login/',views.loginPage,name='loginPage'),
    path('registration/',views.registration,name='registration'),
]