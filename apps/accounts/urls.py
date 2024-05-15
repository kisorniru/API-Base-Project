from django.urls import path

from .views import current_user, login, logout

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('me/', current_user, name='current-user'),
]
