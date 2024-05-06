"""blog_api URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from api.views import BlogPostViewSet
from api.views import WelcomeViewSet
from api.views import CreateUserView


router = DefaultRouter()

router.register('posts', BlogPostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeViewSet.as_view(), name='welcome'),
    path('api/register/', CreateUserView.as_view(), name='register'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
