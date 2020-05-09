from django.urls import include, path
from login import views as view_auth

urlpatterns = [
    path("accounts/register/", view_auth.register, name="register"),
    path("accounts/login/", view_auth.login_view, name='login'),
    path("accounts/logout/", view_auth.logout_view, name='logout'),
]
