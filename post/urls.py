from django.urls import path, include
from .views import PostListView, PostDetialView, PostCreateView, PostUpdateView, PostDeleteView
from review import views as review_view

urlpatterns = [
    path('', PostListView.as_view(), name='post_home'),
    path('post/<int:pk>/', PostDetialView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:post>/review/', review_view.create_review, name='review_create'),
    path('post/<int:pk>/review/update/', review_view.ReviewUpdate.as_view(), name='review_update'),
    path('api/', include('post.api.urls')),
]
