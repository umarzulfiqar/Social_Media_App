from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.UserProfileView, basename='profile')

urlpatterns = [
    path('register/',views.RegisterUser.as_view(),name='register-user'),
    path('login/', views.Login.as_view(), name="login"),
    path('', include(router.urls)),
    path('follow/',views.FollowView.as_view(), name="follow-user"),
    path('unfollow/<int:user_id>/', views.UnFollowView.as_view(), name="unfollow-user")
]
