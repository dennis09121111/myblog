from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('post.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='user_register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user_logout'),
    path('profile/', user_views.profile, name='user_profile'),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
