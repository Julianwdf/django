from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
]

# after store is nothing so blank ''
