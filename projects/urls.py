from . import views
from django.urls import include, path

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
]