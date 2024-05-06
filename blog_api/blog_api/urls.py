from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from api.views import BlogPostViewSet, WelcomeView, CreateUserView

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeView.as_view(), name='welcome'),
    path('api/', include(router.urls)),
    path('api/register/', CreateUserView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
