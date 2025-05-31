from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AuthView, CustomLoginView


urlpatterns = [
    path(
        "auth/login/",
        CustomLoginView.as_view(redirect_authenticated_user=True),
        name="auth-login-basic",
    ),
    path(
        'auth/logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        "auth/register/",
        AuthView.as_view(template_name="auth_register_basic.html"),
        name="auth-register-basic",
    ),
    path(
        "auth/forgot_password/",
        AuthView.as_view(template_name="auth_forgot_password_basic.html"),
        name="auth-forgot-password-basic",
    ),
]
