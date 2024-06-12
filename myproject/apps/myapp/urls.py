from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.myapp.views import AuthorViewSet, BookViewSet

# Definir un router
router = DefaultRouter()
router.register(r'author', AuthorViewSet)
router.register(r'book', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]