from django.urls import path
from . import views

urlpatterns = [
    path('post-create/',views.PostListCreate.as_view(),name="create-post"),
    path('postscrud/<uuid:pk>/',views.PostDetail.as_view(),name="crud-post"),
    path('<uuid:id>/comments/', views.CommentView.as_view(), name="create-comment"),
    path('comments/<uuid:pk>/delete/',views.CommentDeleteView.as_view(), name="delete-comment"),
    path('<uuid:pk>/liketoggle/',views.LikeView.as_view(), name="like-post"),

]
