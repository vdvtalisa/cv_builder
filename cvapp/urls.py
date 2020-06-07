from django.urls import path
from . import views


urlpatterns = (
    path("view", views.cv_view, name="cv_view"),
    path("", views.cv_form, name="cv_form"),
    path("register", views.register_page, name="register"),
    path("login", views.login_page, name="login"),
    path("logout", views.sign_out, name="logout")

)
