from django.urls import path

from backend.users.views import GetCSRFToken, SignUpAPIView, SignInAPIView, LogoutAPIView, GetCurrentUserDataAPIView

app_name = "users"

urlpatterns = [
    path('csrf/', GetCSRFToken.as_view(), name='csrf'),
    path("signup/", SignUpAPIView.as_view(), name='signup'),
    path("signin/", SignInAPIView.as_view(), name='signin'),
    path("logout/", LogoutAPIView.as_view(), name='logout'),
    path("me/", GetCurrentUserDataAPIView.as_view(), name='current-user'),
]
