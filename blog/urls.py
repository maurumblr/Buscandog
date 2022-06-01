from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', views.PostListView.as_view(), name='blog-home'),
    path('<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog-detail-post'),
    path('post/new/', views.PostCreateView.as_view(), name='blog-create-post'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='blog-update-post'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='blog-delete-post'),
    
]