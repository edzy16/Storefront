from django.urls import path
from . import views

#urlconf for the playground app
urlpatterns = [
    path('hello/', views.say_hello),
    ]