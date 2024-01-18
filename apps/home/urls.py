from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.index, name="home_index"),
    path("login/", views.login_h, name="home_login"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="home/login.html", next_page="home_index"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="home_index"), name="logout")
]
