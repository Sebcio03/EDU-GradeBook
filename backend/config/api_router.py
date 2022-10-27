from django.urls import path, include


urlpatterns = [path('users/', include('backend.users.urls'))]
