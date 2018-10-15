from django.urls import path, include
from .views import PostListView, PostDetialView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_home'),
    path('post/<int:pk>/', PostDetialView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('api/', include('post.api.urls')),
]
