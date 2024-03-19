from django.urls import path

from .views import echo, health_check

app_name = 'api'

urlpatterns = [
    path('health/', health_check, name='health'),
    path('echo/', echo, name='echo'),
]
