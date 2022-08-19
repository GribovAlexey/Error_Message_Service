from django.urls import path

from . import class_views, views


app_name = 'message_app'
urlpatterns = [
    path('view/', views.index_view, name='index'),
    path(
        'class_view/',
        class_views.MessageFormView.as_view(),
        name='class_view',
    ),
]
