from django.urls import path
from . import views

urlpatterns = [
    path('post-create/',views.PostListCreate.as_view(),name="create-post"),
    path('posts/<uuid:pk>/',views.PostDetail.as_view())
]
