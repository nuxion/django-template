from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home_index"),
    path("login/", views.login_h, name="home_login"),
]
