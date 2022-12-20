from django.urls import path, include


urlpatterns = [
    path('users/', include('backend.users.urls')),
    path('organizations/', include('backend.organizations.urls')),
]
