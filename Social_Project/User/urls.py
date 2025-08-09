from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterUser.as_view(),name='register-user'),
    path('login/', views.Login.as_view(), name="login")
]
