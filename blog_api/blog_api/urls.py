"""blog_api URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import BlogPostViewSet

router = DefaultRouter()

router.register('posts', BlogPostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
