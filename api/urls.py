from django.urls import path
from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post_list_api'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='post_detail_api'),
]
