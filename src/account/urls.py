from django.urls import path

from . import views

urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("profile/",views.profile,name="profile"),
    path("edit_address/",views.edit_address,name="edit_address"),
    path("remove_address/<int:id>",views.remove_address,name="remove_address"),
]