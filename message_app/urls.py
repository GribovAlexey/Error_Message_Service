from django.urls import path

from . import views


app_name = 'message_app'
urlpatterns = [
    path('', views.index_view, name='index'),
]
