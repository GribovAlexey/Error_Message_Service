from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

urlpatterns = [
    path('message/', views.MessageCreateView.as_view(), name='create_message'),
]
