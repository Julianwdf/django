from django.urls import path
from . import views

urlpatterns = [
    path('', views.oxford, name='oxford')
]
