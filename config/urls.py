from django.urls import include, path

urlpatterns = [
    path('api/', include('apps.api.urls')),
    path('api/auth/', include('apps.accounts.urls')),
]
